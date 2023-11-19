
import collections
import pickle

from . import utils


_logger = utils.get_console_logger(__name__)

ActionCall = collections.namedtuple('ActionCall', ('name', 'params'))


class RCPI:
    def __init__(self):
        self.actions = {}

    def add_action(self, name: str, func) -> bool:
        if self.actions.get(name, None) is None:
            self.actions[name] = func
            return True
        else:
            _logger.error(f'Action named "{name}" is already added')
            return False

    def perform(self, ac: ActionCall):
        if self.actions.get(ac.name, None) is None:
            _logger.error(f'Action called "{ac.name}" was not found')
            return None
        else:
            return self.actions[ac.name](*ac.params)
        
    @staticmethod
    def encode(action: str, *params) -> str:
        pc = len(params)
        encoded = f'{action};'
        for i in range(pc):
            bp = [str(byte) for byte in pickle.dumps(params[i])]
            encoded += f'{",".join(bp)}'
            if i != pc - 1:
                encoded += ';'
        return encoded

    @staticmethod
    def decode(text: str) -> ActionCall:
        name, *strp = text.split(';')
        pc = len(strp)
        decp = [None] * pc
        for i in range(pc):
            bp = [int(sb) for sb in strp[i].split(',')]
            decp[i] = pickle.loads(bytes(bp))
        return ActionCall(name, decp)
