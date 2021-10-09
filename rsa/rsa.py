from mod_exp import ModularExponentiation as me

class RSA:

	@staticmethod
	def encrypt(m, e, n):
		return me().mod_exp(m, e, n)

	@staticmethod
	def decrypt(c, d, n):
		return me().mod_exp(c, d, n)
