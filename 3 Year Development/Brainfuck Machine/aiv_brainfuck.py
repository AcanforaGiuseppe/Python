import unittest

from brainfuck import BrainfuckMachine


class LessonTest(unittest.TestCase):

    def setUp(self):
        self.vm = BrainfuckMachine(64)

    def test_plus(self):
        self.vm.code = '++'
        self.vm.run()
        self.assertEqual(self.vm.tape[0], 2)

    def test_minus(self):
        self.vm.code = '++-'
        self.vm.run()
        self.assertEqual(self.vm.tape[0], 1)

    def test_right_simple(self):
        self.vm.code = '>'
        self.vm.run()
        self.assertEqual(self.vm.head, 1)

    def test_right(self):
        self.vm.code = '>++-'
        self.vm.run()
        self.assertEqual(self.vm.tape[0], 0)
        self.assertEqual(self.vm.tape[1], 1)

    def test_left(self):
        self.vm.code = '>>><<++++'
        self.vm.run()
        self.assertEqual(self.vm.tape[1], 4)

    def test_left_overflow(self):
        self.vm.code = '<'
        self.assertRaises(BrainfuckMachine.HeadOverflow, self.vm.run)

    def test_right_overflow(self):
        self.vm.code = '>' * 65
        self.assertRaises(BrainfuckMachine.HeadOverflow, self.vm.run)

    def test_loop(self):
        self.vm.code = '++[>+++<-]>--'
        self.vm.run()
        self.assertEqual(self.vm.tape[1], 4)

    def test_loop_broken(self):
        self.vm.code = '[['
        self.assertRaises(BrainfuckMachine.BracketMismatch, self.vm.run)

    def test_inner_loop(self):
        self.vm.code = '++>+++<[>[>+++++<-]<-]>>--'
        self.vm.run()
        self.assertEqual(self.vm.tape[2], 13)

    def test_cell_overflow_minus(self):
        self.vm.code = '-'
        self.vm.run()
        self.assertEqual(self.vm.tape[0], 255)

    def test_cell_overflow_minus2(self):
        self.vm.code = '--'
        self.vm.run()
        self.assertEqual(self.vm.tape[0], 254)

    def test_cell_overflow_plus(self):
        self.vm.code = '--+++'
        self.vm.run()
        self.assertEqual(self.vm.tape[0], 1)


if __name__ == '__main__':
    unittest.main()
