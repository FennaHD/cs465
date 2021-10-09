import unittest
from rsa import RSA as rsa


class RSATest(unittest.TestCase):

	def test_encryption_positive(self):
		self.assertEqual(183, rsa.encrypt(72, 3, 187))

	def test_encryption_negative(self):
		self.assertNotEqual(182, rsa.encrypt(72, 3, 187))

	def test_decryption_positive(self):
		self.assertEqual(72, rsa.decrypt(183, 107, 187))

	def test_decryption_negative(self):
		self.assertNotEqual(71, rsa.decrypt(183, 107, 187))