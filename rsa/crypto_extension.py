from Cryptodome.Util import number
from extended_euclidean_algorithm import ExtendedEuclideanAlgorithm as eua
from mod_exp import ModularExponentiation


class CryptoExtension:

	@staticmethod
	def generatePairRelativelyPrimeTo(e):
		"""
		Generates p and q for the RSA algorithm, where p != q and (p-1)(q-1) is relatively prime to e.
		"""
		p = number.getPrime(512)
		q = number.getPrime(512)
		while True:
			gcd, d, k = eua.extended_gcd(e, (p-1)*(q-1))
			if q != p and gcd == 1:
				break
		return p, q

	@staticmethod
	def verifyNumsLessThanN(n, e, d):
		"""
		Verifies that for some values m where m < n, ((m^e%n)^d)%n == m.
		"""
		m1 = n-1
		m2 = n//2
		m3 = 100 # just some arbitrary number
		return all(list(filter(lambda a: CryptoExtension.__verificationHelper(a, n, e, d), [m1, m2, m3])))

	@staticmethod
	def __verificationHelper(m, n, e, d):
		"""
		Verifies that for a single value m where m < n, ((m^e%n)^d)%n == m.
		"""
		me = ModularExponentiation()
		return me.mod_exp(me.mod_exp(m, e, n), d, n) == m