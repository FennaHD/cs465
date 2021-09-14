from decrypter import Decrypter
import unittest


class DecrypterTest(unittest.TestCase):

	decrypter = Decrypter()

	def test_integration_128bits_positive(self):
		self.assertEqual("00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff",
		                 self.decrypter.decrypt(word= "69 c4 e0 d8 6a 7b 04 30 d8 cd b7 80 70 b4 c5 5a",
		                             cipher_key= "00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f"))

	def test_integration_192bits_positive(self):
		self.assertNotEqual("00 00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff",  # this last byte is different
		                    self.decrypter.decrypt(word="dd a9 7c a4 86 4c df e0 6e af 70 a0 ec 0d 71 91",
		                                           cipher_key="00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17"))

	def test_integration_256bits_positive(self):
		self.assertNotEqual("00 00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff",  # this last byte is different
		                    self.decrypter.decrypt(word="8e a2 b7 ca 51 67 45 bf ea fc 49 90 4b 49 60 89",
		                                           cipher_key="00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f"))

	def test_integration_negative(self):
		self.assertNotEqual("00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ee", # this last byte is different
		                 self.decrypter.decrypt(word= "69 c4 e0 d8 6a 7b 04 30 d8 cd b7 80 70 b4 c5 5a",
		                             cipher_key= "00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f"))