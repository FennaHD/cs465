class ModularExponentiation:
	"""
	Holds the logic and the cache used in modular exponentiation.
	The cache's key is an exponent, and its value is g^[key] mod p.
	This way we never compute the same number twice. The cache will
	have at most log2(a) - 1 + log2(a) keys.
	"""

	cache = {}

	def mod_exp(self, g, a, p):
		self.cache = {}
		return self.__mod_exp_helper(g, a, p)

	def __mod_exp_helper(self, g, a, p):
		if a in self.cache:
			pass
		elif a == 1:
			self.cache[a] = g % p
		else:
			first_term = self.__get_or_compute_and_save(g, a // 2, p)
			second_term = first_term if a % 2 == 0 else self.__get_or_compute_and_save(g, (a // 2) + 1, p)
			self.cache[a] = (first_term * second_term) % p
		return self.cache[a]

	def __get_or_compute_and_save(self, g, a, p):
		if a not in self.cache:
			self.cache[a] = self.__mod_exp_helper(g, a, p)
		return self.cache[a]