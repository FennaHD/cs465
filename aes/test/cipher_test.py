from cipher import Cipher
import unittest


class CipherTest(unittest.TestCase):

	cph = Cipher()

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

		self.mix_columns_initial_state = [[0xd4, 0xbf, 0x5d, 0x30],
		                                 [0xe0, 0xb4, 0x52, 0xae],
		                                 [0xb8, 0x41, 0x11, 0xf1],
		                                 [0x1e, 0x27, 0x98, 0xe5]]

		self.add_round_key_initial_state = [[0x04, 0x66, 0x81, 0xe5],
		                                    [0xe0, 0xcb, 0x19, 0x9a],
		                                    [0x48, 0xf8, 0xd3, 0x7a],
		                                    [0x28, 0x06, 0x26, 0x4c]]

		self.add_round_key_initial_round_key = [[0xa0, 0xfa, 0xfe, 0x17],
		                                        [0x88, 0x54, 0x2c, 0xb1],
		                                        [0x23, 0xa3, 0x39, 0x39],
		                                        [0x2a, 0x6c, 0x76, 0x05]]

	def test_sub_byte_positive(self):
		expected = [[0xd4, 0x27, 0x11, 0xae],
		            [0xe0, 0xbf, 0x98, 0xf1],
		            [0xb8, 0xb4, 0x5d, 0xe5],
		            [0x1e, 0x41, 0x52, 0x30]]
		self.assertEqual(expected, self.cph.sub_bytes(self.sub_byte_initial_state))

	def test_sub_byte_negative(self):
		expected = [[0xd4, 0x27, 0x11, 0xae],
		            [0xe0, 0xbf, 0x98, 0xf1],
		            [0xb8, 0xb4, 0x5d, 0xe5],
		            [0x1e, 0x41, 0x52, 0x33]] # this last byte is different
		self.assertNotEqual(expected, self.cph.sub_bytes(self.sub_byte_initial_state))

	def test_shift_rows_positive(self):
		expected = [[0xd4, 0xbf, 0x5d, 0x30],
		            [0xe0, 0xb4, 0x52, 0xae],
		            [0xb8, 0x41, 0x11, 0xf1],
		            [0x1e, 0x27, 0x98, 0xe5]]
		self.assertEqual(expected, self.cph.shift_rows(self.shift_rows_initial_state))

	def test_shift_rows_negative(self):
		expected = [[0xd4, 0xbf, 0x5d, 0x30],
		            [0xe0, 0xb4, 0x52, 0xae],
		            [0xb8, 0x41, 0x11, 0xf1],
		            [0x1e, 0x27, 0x98, 0xee]] # this last byte is different
		self.assertNotEqual(expected, self.cph.shift_rows(self.shift_rows_initial_state))

	def test_mix_columns_positive(self):
		expected = [[0x04, 0x66, 0x81, 0xe5],
		            [0xe0, 0xcb, 0x19, 0x9a],
		            [0x48, 0xf8, 0xd3, 0x7a],
		            [0x28, 0x06, 0x26, 0x4c]]
		self.assertEqual(expected, self.cph.mix_columns(self.mix_columns_initial_state))

	def test_mix_columns_negative(self):
		expected = [[0x04, 0x66, 0x81, 0xe5],
		            [0xe0, 0xcb, 0x19, 0x9a],
		            [0x48, 0xf8, 0xd3, 0x7a],
		            [0x28, 0x06, 0x26, 0x44]] # this last byte is different
		self.assertNotEqual(expected, self.cph.mix_columns(self.mix_columns_initial_state))

	def test_add_round_key_positive(self):
		expected = [[0xa4, 0x9c, 0x7f, 0xf2],
		            [0x68, 0x9f, 0x35, 0x2b],
		            [0x6b, 0x5b, 0xea, 0x43],
		            [0x02, 0x6a, 0x50, 0x49]]
		self.assertEqual(expected, self.cph.add_round_key(self.add_round_key_initial_state, self.add_round_key_initial_round_key))

	def test_add_round_key_negative(self):
		expected = [[0xa4, 0x9c, 0x7f, 0xf2],
		            [0x68, 0x9f, 0x35, 0x2b],
		            [0x6b, 0x5b, 0xea, 0x43],
		            [0x02, 0x6a, 0x50, 0x44]] # this last byte is different
		self.assertNotEqual(expected, self.cph.add_round_key(self.add_round_key_initial_state, self.add_round_key_initial_round_key))


if __name__ == '__main__':
	unittest.main()