from key_expansion_manager import KeyExpansionManager
import unittest


class KeyExpansionManagerTest(unittest.TestCase):
	kem = KeyExpansionManager()

	def test_words(self):
		cipher_key = "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"
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

	# def test_xor_positive(self):
	# 	# Multiple tests because I was having issues when writing the method, make sure it's good.
	# 	self.assertEqual([0x8b, 0x84, 0xeb, 0x01], self.kem.xor1([0x8a, 0x84, 0xeb, 0x01], 1))
	# 	self.assertEqual([0x52, 0x38, 0x6b, 0xe5], self.kem.xor1([0x50, 0x38, 0x6b, 0xe5], 2))
	# 	self.assertEqual([0xcf, 0x42, 0xd2, 0x8f], self.kem.xor1([0xcb, 0x42, 0xd2, 0x8f], 3))
	# 	self.assertEqual([0xd2, 0xc4, 0xe2, 0x3c], self.kem.xor1([0xda, 0xc4, 0xe2, 0x3c], 4))
	# 	self.assertEqual([0x7c, 0x63, 0x9f, 0x5b], self.kem.xor1([0x4a, 0x63, 0x9f, 0x5b], 10))
	#
	# def test_xor_negative(self):
	# 	self.assertNotEqual([0x8a, 0x84, 0xeb, 0x01], self.kem.xor1([0x8a, 0x84, 0xeb, 0x01], 1))

	def test_get_all_words_positive(self):
		all_words = self.kem.get_all_words("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c")
		self.assertEqual(44, len(all_words))
		self.assertEqual([0xa0, 0xfa, 0xfe, 0x17], all_words[4])
		self.assertEqual([0xca, 0xf2, 0xb8, 0xbc], all_words[22])
		self.assertEqual([0x84, 0xa6, 0x4f, 0xb2], all_words[30])
		self.assertEqual([0x19, 0xfa, 0xdc, 0x21], all_words[37])
		self.assertEqual([0xb6, 0x63, 0x0c, 0xa6], all_words[43])

	def test_get_all_words_negative(self):
		all_words = self.kem.get_all_words("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c")
		self.assertNotEqual([0xb6, 0x63, 0x0c, 0xaa], all_words[43])

	def test_get_schedule_positive(self):
		schedule = self.kem.get_schedule("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c")
		expected_state_with_index_1 = [[0xa0, 0xfa, 0xfe, 0x17],
		                               [0x88, 0x54, 0x2c, 0xb1],
		                               [0x23, 0xa3, 0x39, 0x39],
		                               [0x2a, 0x6c, 0x76, 0x05]]
		self.assertEqual(expected_state_with_index_1, schedule[1])

	def test_get_schedule_negative(self):
		schedule = self.kem.get_schedule("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c")
		expected_state_with_index_1 = [[0xa0, 0xfa, 0xfe, 0x17],
		                               [0x88, 0x54, 0x2c, 0xb1],
		                               [0x23, 0xa3, 0x39, 0x39],
		                               [0x2a, 0x6c, 0x76, 0x00]] # this last byte is different
		self.assertNotEqual(expected_state_with_index_1, schedule[1])


if __name__ == '__main__':
	unittest.main()