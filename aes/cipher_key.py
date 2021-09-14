class CipherKey:
	"""
	Holds parameters that change according to the key size
	"""

	def __init__(self, key):
		self.key = key
		self.nb = 4 # number of blocks is constant across key sizes
		num_bytes = len(key.split(" "))
		if num_bytes == 16:
			self.nk = 4 # key length
			self.nr = 10 # number of rounds
		elif num_bytes == 24:
			self.nk = 6
			self.nr = 12
		elif num_bytes == 32:
			self.nk = 8
			self.nr = 14
		else:
			raise Exception("Invalid key size")