from extended_euclidean_algorithm import ExtendedEuclideanAlgorithm as eua
import unittest


class ExtendedGcdTest(unittest.TestCase):

	def test_relatively_prime_positive(self):
		gcd, x, y = eua.extended_gcd(5, 72) # These two are relatively prime
		self.assertEqual(1, gcd)
		self.assertEqual(29, x)

	def test_relatively_prime_negative(self):
		gcd, x, y = eua.extended_gcd(5, 72) # These two are relatively prime
		self.assertNotEqual(5, gcd)
		self.assertNotEqual(30, x)

	def test_not_relatively_prime_positive(self):
		gcd, x, y = eua.extended_gcd(15, 70) # These two are not relatively prime
		self.assertEqual(5, gcd)
		self.assertEqual(5, x)

	def test_not_relatively_prime_negative(self):
		gcd, x, y = eua.extended_gcd(15, 70) # These two are not relatively prime
		self.assertNotEqual(6, gcd)
		self.assertNotEqual(6, x)

	def test_normalize_positive_x_positive(self):
		self.assertEqual(5, eua.normalize(5, 7))

	def test_normalize_positive_x_negative(self):
		self.assertNotEqual(-5, eua.normalize(5, 7))

	def test_normalize_negative_x_positive(self):
		self.assertEqual(2, eua.normalize(-5, 7))

	def test_normalize_negative_x_negative(self):
		self.assertNotEqual(5, eua.normalize(-5, 7))