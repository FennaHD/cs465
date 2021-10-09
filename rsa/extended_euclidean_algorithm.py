
class ExtendedEuclideanAlgorithm:


	@staticmethod
	def extended_gcd(a, b):
		"""
		Implementation of the extended Euclidean algorithm.
		If a nd b are relatively prime then gcd will be equal to 1.
		"""
		if a == 0:
			return b, 0, 1

		gcd, temp_x, temp_y = ExtendedEuclideanAlgorithm.extended_gcd(b % a, a)

		x = temp_y - (b//a) * temp_x
		y = temp_x

		return gcd, x, y

	@staticmethod
	def normalize(d, phi_n):
		"""
		Our RSA algorithm requires d to be a positive integer, so if d is negative
		we add phi_n to it. This works because d % n === (d + phi_n) % n.
		"""
		return d + phi_n if d < 0 else d