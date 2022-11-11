import sys


class BrainfuckMachine:

    class HeadOverflow(Exception):
        pass

    class BracketMismatch(Exception):
        pass

    def defineCommands(self):
        self.tape = [0] * self.tapeSize
        self.head = 0
        self.codeId = 0
        self.counter = 0
        self.code = 0
        self.opCodeIndex = []

    def load(self, fileName):
        self.defineCommands()
        with open(fileName, 'r') as handle:
            self.code = handle.read()

    def __init__(self, tapeSize):
        self.tapeSize = tapeSize
        self.commands = {
            '+': self._cmd_plus,
            '-': self._cmd_minus,
            '>': self._cmd_right,
            '<': self._cmd_left,
            '[': self._cmd_square_open,
            ']': self._cmd_square_closed,
            '.': self._cmd_dot,
        }
        self.defineCommands()

    def _cmd_plus(self):
        self.tape[self.head] += 1
        if self.tape[self.head] > 255:
            self.tape[self.head] = 0

    def _cmd_minus(self):
        self.tape[self.head] -= 1
        if self.tape[self.head] < 0:
            self.tape[self.head] = 255

    def _cmd_right(self):
        self.head += 1

    def _cmd_left(self):
        self.head -= 1

    def _cmd_square_open(self):
        if self.tape[self.head] == 0:
            stack = 0
            for index, symbol in enumerate(self.code[self.codeId:]):
                if symbol == '[':
                    stack += 1
                elif symbol == ']':
                    stack -= 1
                    if stack == 0:
                        self.codeId += index
                        return
            raise BrainfuckMachine.BracketMismatch
            ('Miss matching w/ closing square bracket')

    def _cmd_square_closed(self):
        if self.tape[self.head] != 0:
            stack = 0
            for index, symbol in enumerate(self.code[self.codeId::-1]):
                if symbol == ']':
                    stack += 1
                elif symbol == '[':
                    stack -= 1
                    if stack == 0:
                        self.codeId -= index
                        return
            raise BrainfuckMachine.BracketMismatc
            ('Miss matching w/ opening square bracket')

    def _cmd_dot(self):
        print(chr(self.tape[self.head]), end='')

    def run(self):
        while self.codeId < len(self.code):
            command = self.code[self.codeId]
            if command in self.commands:
                self.counter += 1
                if self.codeId not in self.opCodeIndex:
                    self.opCodeIndex.append(self.codeId)
                self.commands[command]()
                if self.head < 0 or self.head >= len(self.tape):
                    raise BrainfuckMachine.HeadOverflow
                    ('Headoverflow exception')
                    BrainfuckMachine.HeadOverflow().format(self.head)
            self.codeId += 1


if __name__ == '__main__':
    brainfuckMachineInstance = BrainfuckMachine(64)
    for filename in sys.argv[1:]:
        brainfuckMachineInstance.load(filename)
        brainfuckMachineInstance.run()
        print(brainfuckMachineInstance.opCodeIndex,
              brainfuckMachineInstance.counter)
