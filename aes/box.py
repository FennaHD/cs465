from abc import ABC


class Box(ABC):
	"""
	Base class for the S-box and the Inverse S-Box
	"""

	# Must return a 2D array of integers representing bytes
	box: [[int]]

	def transformation(self, byte):
		"""
		Maps a byte to its box implementation transformation.
		E.g. 0x01 returns 0x7c
		"""
		# Format is "0x<nibble1><nibble2>", so we just split on the x and get the last element.
		# hex skips the 0, so we pad the start.
		nibbles = str(hex(byte)).split("x")[-1].rjust(2, "0")
		row, col = box_index(nibbles[0]), box_index(nibbles[1])
		return self.box[row][col]

def box_index(nibble):
	"""
	Given an input nibble as a string, returns the index of its transformation in a box.
	E.g. "0" returns 0, "a" returns 10, "f" returns 16, etc. Naturally, the nibble
	can only have values 0-9 and a-f.
	"""
	# Since ASCII 'a' is 97, then hex 'a' is ASCII 'a' - 87 = 97 - 87 = 10. Same for [b-f]
	return int(nibble) if nibble.isnumeric() else ord(nibble) - 87