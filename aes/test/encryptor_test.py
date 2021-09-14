from encryptor import Encryptor
import unittest


class EncryptorTest(unittest.TestCase):

	encryptor = Encryptor()

	def test_integration_positive(self):
		self.assertEqual("39 25 84 1d 02 dc 09 fb dc 11 85 97 19 6a 0b 32",
		                 self.encryptor.encrypt(word= "32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34",
		                             cipher_key= "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"))

	def test_integration_negative(self):
		self.assertNotEqual("39 25 84 1d 02 dc 09 fb dc 11 85 97 19 6a 0b 33", # this last byte is different
		                 self.encryptor.encrypt(word= "32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34",
		                             cipher_key= "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"))