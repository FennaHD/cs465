import functools as ft


class FFMath:

	"""
	Performs finite field add, which is basically just an XOR
	"""
	@staticmethod
	def add(byte1, byte2):
		return byte1 ^ byte2

	"""
	Equivalent to performing `byte` * 0x02. We do this by performing a left shift. 
	If the result overflows, we remove the highest bit and perform an XOR with 0x1b.
	"""
	@staticmethod
	def x_time(byte):
		left_shifted = byte << 1
		# The & operation removes the highest bit, because otherwise we return a 9 bit number
		return (left_shifted & 0b11111111) ^ 0x1b if left_shifted.bit_length() == 9 else left_shifted

	@staticmethod
	def get_x_time_dict(byte):
		x_time_dict = {0: byte}
		x_time_dict[1] = FFMath.x_time(x_time_dict[0])
		x_time_dict[2] = FFMath.x_time(x_time_dict[1])
		x_time_dict[3] = FFMath.x_time(x_time_dict[2])
		x_time_dict[4] = FFMath.x_time(x_time_dict[3])
		x_time_dict[5] = FFMath.x_time(x_time_dict[4])
		x_time_dict[6] = FFMath.x_time(x_time_dict[5])
		x_time_dict[7] = FFMath.x_time(x_time_dict[6])
		return x_time_dict

	"""
	Given two bytes, returns an array made up of all x_time values of the first byte
	from the set bits of the second byte. E.g. (0x57, 0x13) would return [0xae, 0x07]
	"""
	@staticmethod
	def get_intermediate_results(byte1, byte2):
		# Originally bin(byte2) will return a string in the format "0b<8 bits>".
		# This format makes the bits easier to read for a human, but it's harder
		# to use for what we want. The problem with this is that the string has a
		# padding ("0b") and the bits are in reverse order from what we can use.
		# So first we remove the padding, reverse the string, and then add padding
		# as zeros.
		bits = bin(byte2)[2:][::-1].ljust(8, '0')
		x_time_dict = FFMath.get_x_time_dict(byte1)
		intermediate_results = []
		# We only care about the bits that are set
		for index, bit in enumerate(bits):
			if bit == '1':
				intermediate_results.append(x_time_dict[index])
		return intermediate_results

	"""
	Perform finite field multiplication
	"""
	@staticmethod
	def multiply(byte1, byte2):
		return ft.reduce(lambda a, b: FFMath.add(a, b), FFMath.get_intermediate_results(byte1, byte2))
