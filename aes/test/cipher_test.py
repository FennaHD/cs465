from cipher import Cipher
import unittest


class CipherTest(unittest.TestCase):

	# Since we are testing with states we already know the conversions of, each operation will be tested using a different initial state.
	# This is inefficient, but visually better than initializing each state twice (assuming two test cases per operation).
	def setUp(self):
		self.sub_byte_initial_state = [[0x19, 0x3d, 0xe3, 0xbe],
		                               [0xa0, 0xf4, 0xe2, 0x2b],
		                               [0x9a, 0xc6, 0x8d, 0x2a],
		                               [0xe9, 0xf8, 0x48, 0x08]]

		self.shift_rows_initial_state = [[0xd4, 0x27, 0x11, 0xae],
		                                 [0xe0, 0xbf, 0x98, 0xf1],
		                                 [0xb8, 0xb4, 0x5d, 0xe5],
		                                 [0x1e, 0x41, 0x52, 0x30]]

	def test_sub_byte_positive(self):
		expected = [[0xd4, 0x27, 0x11, 0xae],
		            [0xe0, 0xbf, 0x98, 0xf1],
		            [0xb8, 0xb4, 0x5d, 0xe5],
		            [0x1e, 0x41, 0x52, 0x30]]
		self.assertEqual(expected, Cipher.sub_bytes(self.sub_byte_initial_state))

	def test_sub_byte_negative(self):
		expected = [[0xd4, 0x27, 0x11, 0xae],
		            [0xe0, 0xbf, 0x98, 0xf1],
		            [0xb8, 0xb4, 0x5d, 0xe5],
		            [0x1e, 0x41, 0x52, 0x33]] # this last byte is different
		self.assertNotEqual(expected, Cipher.sub_bytes(self.sub_byte_initial_state))

	def test_shift_rows_positive(self):
		expected = [[0xd4, 0xbf, 0x5d, 0x30],
		            [0xe0, 0xb4, 0x52, 0xae],
		            [0xb8, 0x41, 0x11, 0xf1],
		            [0x1e, 0x27, 0x98, 0xe5]]
		self.assertEqual(expected, Cipher.shift_rows(self.shift_rows_initial_state))

	def test_shift_rows_negative(self):
		expected = [[0xd4, 0xbf, 0x5d, 0x30],
		            [0xe0, 0xb4, 0x52, 0xae],
		            [0xb8, 0x41, 0x11, 0xf1],
		            [0x1e, 0x27, 0x98, 0xee]] # this last byte is different
		self.assertNotEqual(expected, Cipher.shift_rows(self.shift_rows_initial_state))


if __name__ == '__main__':
	unittest.main()