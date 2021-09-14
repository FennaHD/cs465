from formatter import Formatter as ftr
import unittest


class FormatterTest(unittest.TestCase):

	def setUp(self):
		self.initial_state = [[0x2b, 0x7e, 0x15, 0x16],
		                      [0x28, 0xae, 0xd2, 0xa6],
		                      [0xab, 0xf7, 0x15, 0x88],
		                      [0x09, 0xcf, 0x4f, 0x3c]]

	def test_str_from_state_positive(self):
		self.assertEqual("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c", ftr.str_from_state(self.initial_state))

	def test_str_from_state_negative(self):
		self.assertNotEqual("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 33", ftr.str_from_state(self.initial_state))

	def test_state_from_str_positive(self):
		self.assertEqual(self.initial_state, ftr.state_from_str("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 33"))

	def test_state_from_str_negative(self):
		expected = [[0x2b, 0x7e, 0x15, 0x16],
		            [0x28, 0xae, 0xd2, 0xa6],
		            [0xab, 0xf7, 0x15, 0x88],
		            [0x09, 0xcf, 0x4f, 0x3c]]
		self.assertNotEqual(expected, ftr.state_from_str("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 33"))


if __name__ == '__main__':
	unittest.main()