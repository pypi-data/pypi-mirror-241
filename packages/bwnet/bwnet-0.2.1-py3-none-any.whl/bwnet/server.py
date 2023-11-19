
import collections
import time
import threading
import types
import socket
import selectors

from . import utils


E_NO_ERROR = 0
E_NOT_INITIALIZED = 1
E_ALREADY_SENDING = 2
E_CLIENT_CLOSED_CONNECTION = 3
E_CLIENT_NOT_FOUND = 4
E_SERVER_IS_FULL = 5
E_TCP_ERROR = 6
E_ALREADY_INITIALIZED = 7
E_INVALID_PORT = 8
E_NULL_RESPONSE = 9

Process = collections.namedtuple('Process', (
        'address',
        'port',
        # Unix timestamp, at which process estabilished the connection.
        # It is sometimes used to distniguish sockets from each other.
        'birthday'
))
Process.__str__ = lambda self: f'{self.address}:{self.port}'

_logger = utils.get_console_logger(__name__)
_sel = None
_handling_thread = None
_lis_sock = None
_loop_iter_dur = None
_max_clients = None
_buffer_size = None
_cl_socks = None  # The index here is respective to next lists below and vice versa.
_cl_procs = None
_cl_buffs = None
_terminate = False
is_initialized = False


def _handle_selector():
    while is_initialized:
        events = _sel.select(timeout=_loop_iter_dur)
        for skey, mask in events:
            if skey.data.is_guest:
                _serve_guest(skey)
            else:
                _serve_client(skey, mask)

def _save_client(sock: socket.socket, proc: Process):
    global _cl_socks, _cl_procs, _cl_data
    for cl_id in range(len(_cl_socks)):
        if _cl_socks[cl_id] is None:
            _cl_socks[cl_id] = sock
            _cl_procs[cl_id] = proc
            _logger.info(f'Saved a new client process {proc}')
            return E_NO_ERROR
    else:
        _logger.error(f'Cannot save a new client process {proc} because server is full')
        return E_SERVER_IS_FULL

def _get_client_info(sock: socket.socket = None, proc: Process = None) -> tuple:
    if sock is None and proc is None:
        _logger.error('Cannot find a client process without any information')
    else:
        for cl_id in range(len(_cl_socks)):
            if (sock and sock == _cl_socks[cl_id]) or (proc and proc == _cl_procs[cl_id]):
                msg = f'socket {_cl_socks[cl_id].fileno()}' if sock is not None else f'client process {_cl_procs[cl_id]}'
                _logger.info(f'Collected information about the {msg}')
                return (cl_id, _cl_socks[cl_id], _cl_procs[cl_id], _cl_buffs[cl_id])
        _logger.error(f'Cannot find a client process using given data')
    return (None, None, None, None)

def _forget_client(sock: socket.socket = None, proc: Process = None) -> int:
    global _cl_socks, _cl_procs, _cl_buffs
    cl_id, cl_sock, cl_proc, _ = _get_client_info(sock=sock, proc=proc)
    if cl_id is not None:
        _sel.unregister(cl_sock)
        cl_sock.close()
        _cl_socks[cl_id] = None
        _cl_procs[cl_id] = None
        _cl_buffs[cl_id] = b''  # Ensure the emptiness.
        _logger.info(f'Forgot the client process {cl_proc}')
        return E_NO_ERROR
    else:
        return E_CLIENT_NOT_FOUND

def _serve_guest(skey: selectors.SelectorKey):
    cl_sock, cl_addr = skey.fileobj.accept()
    cl_sock.setblocking(False)
    cl_proc = Process(*cl_addr, int(time.time()))
    err = _save_client(cl_sock, cl_proc)
    if err == E_SERVER_IS_FULL:
        cl_sock.close()
    elif err == E_NO_ERROR:
        _sel.register(
            cl_sock,
            selectors.EVENT_READ | selectors.EVENT_WRITE,
            data=types.SimpleNamespace(address=cl_addr, is_guest=False)
        )
        on_client_join(cl_proc)

def _serve_client(skey: selectors.SelectorKey, mask: int):
    global _handling_thread, _cl_buffs, _terminate, is_initialized
    cl_is_losing_conn = False
    if mask & selectors.EVENT_READ:
        _, cl_sock, cl_proc, _ = _get_client_info(sock=skey.fileobj)
        if cl_sock is None:
            cl_is_losing_conn = True
        else:
            err = E_NULL_RESPONSE
            try:
                b_msg = cl_sock.recv(_buffer_size)
            except ConnectionResetError:
                _logger.warning(f'Client process {cl_proc} closed the connection')
                err = E_CLIENT_CLOSED_CONNECTION
            request = len(b_msg) == 1 and b_msg[0] == 0
            if len(b_msg) == 0 or request:
                if request:
                    _logger.info(f'Received disconection request from client process {cl_proc}, disconnected')
                else:
                    _logger.warning(f'Null message from client process {cl_proc}, it will be disconnected')
                on_client_quit(cl_proc, err=err)
                _forget_client(proc=cl_proc)
                # Close the server when requested, and when all clients have gone
                if _terminate and not any(_cl_socks):
                    is_initialized = False  # This will halt the handling thread
                    _terminate = False
                    _sel.unregister(_lis_sock)
                    _lis_sock.close()
                    _logger.info('All clients got disconnected and server is now closed')
                return
            else:
                _logger.info(f'Received a message of length {len(b_msg)} from the client process {cl_proc}')
                on_client_message(cl_proc, b_msg.decode())
    if mask & selectors.EVENT_WRITE:
        # If some buffer is filled, make sure it is not this client's.
        if not cl_is_losing_conn and any( ( len(buff) != 0 for buff in _cl_buffs ) ):
            cl_id, cl_sock, cl_proc, cl_buff = _get_client_info(sock=skey.fileobj)
            if len(cl_buff) != 0:
                cl_sock.send(cl_buff)
                _logger.info(f'Sent a message of length {len(cl_buff)} to the client process {cl_proc}')
                _cl_buffs[cl_id] = b''  # Reset the client send buffer.

def init(host: str, port: int, max_clients: int, buffer_size: int = 256, loop_fps: int = 0, show_logs: bool = False) -> tuple:
    global _sel, _handling_thread, _lis_sock, _loop_iter_dur, _max_clients, _buffer_size, _cl_socks, _cl_procs, _cl_buffs, is_initialized
    if is_initialized:
        _logger.warning('Close the server first in order to initialize it again')
        return ( E_ALREADY_INITIALIZED, -1 )
    _logger.disabled = not show_logs
    _sel = selectors.DefaultSelector()
    _lis_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _lis_sock.setblocking(False)
    try:
        _lis_sock.bind((host, port))
    except socket.error as exc:
        _logger.error(f'TCP error {exc.errno} occured when tried to bound address')
        return ( E_TCP_ERROR, exc.errno )
    except OverflowError:
        _logger.error(f'Invalid port (expected 0-65535, got {port})')
        return ( E_INVALID_PORT, -1 )
    _lis_sock.listen()
    _sel.register(
        _lis_sock,
        selectors.EVENT_READ,
        data=types.SimpleNamespace(is_guest=True)
    )
    _loop_iter_dur = 0 if loop_fps == 0 else 1 / loop_fps
    _max_clients = max_clients
    _buffer_size = buffer_size
    _cl_socks = [None] * max_clients
    _cl_procs = [None] * max_clients
    _cl_buffs = [b''] * max_clients
    is_initialized = True
    # Create a thread for listening the selector
    _handling_thread = threading.Thread(target=_handle_selector)
    _handling_thread.start()
    _logger.info('Initialized the server successfuly')
    return ( E_NO_ERROR, -1 )

def close() -> int:
    global _terminate
    if is_initialized:
        for cl_proc in filter(lambda s: s is not None, _cl_procs):
            send(cl_proc, '\0')  # Send termination message
        _terminate = True
        return E_NO_ERROR
    else:
        return E_NOT_INITIALIZED

def disconnect(cp: Process) -> int:
    if is_initialized:
        return _forget_client(proc=cp)
    else:
        return E_NOT_INITIALIZED

def send(cp: Process, msg: str) -> int:
    global _cl_buffs
    if not is_initialized:
        return E_NOT_INITIALIZED
    cl_id, _, cl_proc, cl_buff = _get_client_info(proc=cp)
    if len(cl_buff) == 0:
        _cl_buffs[cl_id] = msg.encode()
        return E_NO_ERROR
    else:
        _logger.warning(f'Already sending a message to the client process {cl_proc}')
        return E_ALREADY_SENDING

def get_clients_count() -> int:
    return len(tuple(filter(lambda clp: clp is not None, _cl_procs)))

def get_client_by_id(cl_id: int) -> Process:
    if cl_id < 0 or cl_id >= get_clients_count():
        _logger.error(f'Cannot get client process by id {cl_id}, which is invalid')
        return None
    return _cl_procs[cl_id]

def on_client_join(cp: Process):
    return

def on_client_message(cp: Process, msg: str):
    return msg

def on_client_quit(cp: Process, err: int):
    return
