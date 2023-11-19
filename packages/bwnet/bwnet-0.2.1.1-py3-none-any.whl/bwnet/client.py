
import threading
import socket
import selectors

from . import utils


E_NO_ERROR = 0
E_NOT_CONNECTED = 1
E_ALREADY_SENDING = 2
E_SERVER_CLOSED_CONNECTION = 3
E_ALREADY_INITIALIZED = 4
E_TCP_ERROR = 6
E_NULL_RESPONSE = 7

_logger = utils.get_console_logger(__name__)
_sel = None
_handling_thread = None
_ser_sock = None
_buffer_size = None
_init_params = None
_loop_iter_dur = None
_send_buffer = b''
is_initialized = False
is_connected = False


def _reinit():
    global _send_buffer, is_initialized, is_connected
    _send_buffer = b''
    is_initialized = False
    is_connected = False
    if is_connected:
        _handling_thread.join()
        _sel.unregister(_ser_sock)
        _ser_sock.close()
    init(*_init_params)

def _handle_selector():
    while is_connected:
        events = _sel.select(timeout=_loop_iter_dur)
        for skey, mask in events:
            _handle_server(skey, mask)

def _handle_server(skey: selectors.SelectorKey, mask: int):
    global _send_buffer, _allow_null
    ss: socket.socket = skey.fileobj
    if mask & selectors.EVENT_READ:
        err = E_NULL_RESPONSE
        try:
            # Packet overloading is not taken into account yet ...
            # And it will not propably be in the nearest future ...
            b_msg: bytes = ss.recv(_buffer_size)
        except ConnectionResetError:
            err = E_SERVER_CLOSED_CONNECTION
            _logger.warning('Server closed the connection')
        if len(b_msg) == 1 and b_msg[0] == 0:
            # Server can force the disconnection by sending '\0' (null character)
            _logger.info('Received disconnection request from the server, sent confirmation')
            disconnect()
        elif len(b_msg) == 0:
            # Normal exit procedure on some error
            _logger.warning('Null message from the server, the client will be disconnected')
            on_server_quit(err=err)
            _reinit()
            return
        else:
            _logger.info(f'Received a message of length {len(b_msg)} from the server')
            on_server_message(b_msg.decode())
    if mask & selectors.EVENT_WRITE:
        if len(_send_buffer) != 0:
            ss.send(_send_buffer)
            _logger.info(f'Sent a message of length {len(_send_buffer)} to the server')
            _send_buffer = b''

def init(buffer_size: int = 256, loop_fps: int = 0, show_logs: bool = False) -> int:
    global _sel, _ser_sock, _buffer_size, _init_params, _loop_iter_dur, is_initialized
    if is_initialized:
        _logger.warning('Close the client first in order to initialize it again')
        return E_ALREADY_INITIALIZED
    _logger.disabled = not show_logs
    _sel = selectors.DefaultSelector()
    _ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _ser_sock.setblocking(False)
    _buffer_size = buffer_size
    _init_params = (buffer_size, loop_fps, show_logs)
    _loop_iter_dur = 0 if loop_fps == 0 else 1 / loop_fps
    _logger.info('Initialized the client successfuly')
    is_initialized = True
    return E_NO_ERROR

def connect(host: str, port: int) -> int:
    global is_connected, _handling_thread
    err = _ser_sock.connect_ex((host, port))
    if err == 0:
        _sel.register(
            _ser_sock,
            selectors.EVENT_READ | selectors.EVENT_WRITE,
            data=None
        )
        _logger.info(f'Connected to the server host {host} on port {port}')
        is_connected = True
        # Create a thread for listening the selector
        _handling_thread = threading.Thread(target=_handle_selector)
        _handling_thread.start()
    # Socket error 115 "Operation in progress" - deal with it by trying again.
    elif err == 115:
        _logger.warning('Connection in progress, checking if finished')
        return connect(host, port)
    else:
        _logger.error(f'TCP error {err} occured when tried connecting to the server')
        return E_TCP_ERROR
    return E_NO_ERROR

def disconnect() -> int:
    global _allow_null
    if is_connected:
        _logger.info('Disconnected from the server, reinstantiating the client socket')
        send('\0')  # Send termination message
        return E_NO_ERROR
    else:
        _logger.error('Cannot disconnect because client is not yet connected')
        return E_NOT_CONNECTED
    
def send(msg: str) -> int:
    global _send_buffer
    if is_connected:
        if len(_send_buffer) == 0:
            _send_buffer = msg.encode()
            return E_NO_ERROR
        else:
            _logger.info('Cannot send a message because client is already sending a one')
            return E_ALREADY_SENDING
    else:
        return E_NOT_CONNECTED

def on_server_message(msg: str):
    return msg

def on_server_quit(err: int):
    return
