from cipher_key import CipherKey
from key_expander import KeyExpander
import unittest


class KeyExpansionManagerTest(unittest.TestCase):
	kem = KeyExpander()

	def test_words(self):
		cipher_key = CipherKey("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c")
		self.assertEqual(
			[[0x2b, 0x7e, 0x15, 0x16], [0x28, 0xae, 0xd2, 0xa6], [0xab, 0xf7, 0x15, 0x88], [0x09, 0xcf, 0x4f, 0x3c]],
			self.kem.get_initial_words(cipher_key))

	def test_sub_word_positive(self):
		self.assertEqual([0x8a, 0x84, 0xeb, 0x01], self.kem.sub_word([0xcf, 0x4f, 0x3c, 0x09]))

	def test_sub_word_negative(self):
		self.assertNotEqual([0xcf, 0x4f, 0x3c, 0x09], self.kem.sub_word([0xcf, 0x4f, 0x3c, 0x09]))

	def test_rot_word_positive(self):
		self.assertEqual([0xcf, 0x4f, 0x3c, 0x09], self.kem.rot_word([0x09, 0xcf, 0x4f, 0x3c]))

	def test_rot_word_negative(self):
		self.assertNotEqual([0x09, 0xcf, 0x4f, 0x3c], self.kem.rot_word([0x09, 0xcf, 0x4f, 0x3c]))

	def test_get_all_words_positive(self):
		all_words = self.kem.get_all_words(CipherKey("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"))
		self.assertEqual(44, len(all_words))
		self.assertEqual([0xa0, 0xfa, 0xfe, 0x17], all_words[4])
		self.assertEqual([0xca, 0xf2, 0xb8, 0xbc], all_words[22])
		self.assertEqual([0x84, 0xa6, 0x4f, 0xb2], all_words[30])
		self.assertEqual([0x19, 0xfa, 0xdc, 0x21], all_words[37])
		self.assertEqual([0xb6, 0x63, 0x0c, 0xa6], all_words[43])

	def test_get_all_words_negative(self):
		all_words = self.kem.get_all_words(CipherKey("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"))
		self.assertNotEqual([0xb6, 0x63, 0x0c, 0xaa], all_words[43])

	def test_get_schedule_128bits_positive(self):
		schedule = self.kem.get_schedule(CipherKey("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"))
		expected_state_with_index_1 = [[0xa0, 0xfa, 0xfe, 0x17],
		                               [0x88, 0x54, 0x2c, 0xb1],
		                               [0x23, 0xa3, 0x39, 0x39],
		                               [0x2a, 0x6c, 0x76, 0x05]]
		self.assertEqual(expected_state_with_index_1, schedule[1])

	def test_get_schedule_192bits_positive(self):
		schedule = self.kem.get_schedule(CipherKey("00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17"))
		expected_state_with_index_1 = [[0x10, 0x11, 0x12, 0x13],
		                               [0x14, 0x15, 0x16, 0x17],
		                               [0x58, 0x46, 0xf2, 0xf9],
		                               [0x5c, 0x43, 0xf4, 0xfe]]
		expected_final_state = [[0xa4, 0x97, 0x0a, 0x33],
		                        [0x1a, 0x78, 0xdc, 0x09],
		                        [0xc4, 0x18, 0xc2, 0x71],
		                        [0xe3, 0xa4, 0x1d, 0x5d]]
		self.assertEqual(expected_state_with_index_1, schedule[1])
		self.assertEqual(expected_final_state, schedule[12])

	def test_get_schedule_256bits_positive(self):
		schedule = self.kem.get_schedule(CipherKey("00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f"))
		expected_state_with_index_1 = [[0x10, 0x11, 0x12, 0x13],
		                               [0x14, 0x15, 0x16, 0x17],
		                               [0x18, 0x19, 0x1a, 0x1b],
		                               [0x1c, 0x1d, 0x1e, 0x1f]]
		expected_final_state = [[0x24, 0xfc, 0x79, 0xcc],
		                        [0xbf, 0x09, 0x79, 0xe9],
		                        [0x37, 0x1a, 0xc2, 0x3c],
		                        [0x6d, 0x68, 0xde, 0x36]]
		self.assertEqual(expected_state_with_index_1, schedule[1])
		self.assertEqual(expected_final_state, schedule[14])

	def test_get_schedule_negative(self):
		schedule = self.kem.get_schedule(CipherKey("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"))
		expected_state_with_index_1 = [[0xa0, 0xfa, 0xfe, 0x17],
		                               [0x88, 0x54, 0x2c, 0xb1],
		                               [0x23, 0xa3, 0x39, 0x39],
		                               [0x2a, 0x6c, 0x76, 0x00]] # this last byte is different
		self.assertNotEqual(expected_state_with_index_1, schedule[1])


if __name__ == '__main__':
	unittest.main()