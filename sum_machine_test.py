import unittest
from sum_machine import SumMachine
 
class SumMachineTest(unittest.TestCase):

    def setUp(self):
        self.machine = SumMachine() 

    def test_sum_two_numbers(self):
        result = self.machine.do_your_stuff(2,2)
        self.assertEqual(4, result)

    def test_fails_when_input_is_string(self):
        self.assertRaises(ValueError, self.machine.do_your_stuff, 'two', 'two')
