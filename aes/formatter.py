import functools as ft

class Formatter:
	"""
	Helper class that doesn't apply any transformations, but can turn bytes into its
	string representation, a state into its string representation, and vice versa.
	"""

	@staticmethod
	def str_from_state(state):
		"""
		Given an input state as a 2D array of integer bytes, return a string of comma separated hex values.

		[[0x2b, 0x7e, 0x15, 0x16],
		[0x28, 0xae, 0xd2, 0xa6],   -->  "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c"
		[0xab, 0xf7, 0x15, 0x88],
		[0x09, 0xcf, 0x4f, 0x3c]]
		"""
		flat_map = ft.reduce(lambda a, b: a + b, state)
		str_array = list(map(lambda byte: Formatter.hex_str_from_byte(byte), flat_map))
		return " ".join(str_array)

	@staticmethod
	def state_from_str(word):
		"""
		Splits key into an array of words, while also reformatting them to be hex integers.
		cipher_key is expected to be a single-space separated string of bytes. E.g.
		"2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c". We can't work with this key, so
		we must first convert it to a format we can use. We decided on a 2D array so that
		with the input from above:

		From input "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c":

		2b 28 ab 09       [[0x2b, 0x7e, 0x15, 0x16],
		7e ae f7 cf  -->   [0x28, 0xae, 0xd2, 0xa6],
		15 d2 15 4f        [0xab, 0xf7, 0x15, 0x88],
		16 a6 88 3c        [0x09, 0xcf, 0x4f, 0x3c]]

		"""
		# turn "<nibble><nibble>" into integer 0x<nibble><nibble>
		byte_array = list(map(lambda a: int(a, 16), word.split(" ")))
		i = 0
		nk = 4
		w = []
		while i < nk:
			i4 = 4 * i
			w.append(byte_array[i4:i4 + 4])
			i += 1
		return w

	@staticmethod
	def hex_str_from_byte(byte):
		"""
		Given an integer input representing a byte return its hex string representation.

		0x2b --> "2b"
		"""
		return str(hex(byte)).split("x")[-1].rjust(2, "0")

	@staticmethod
	def formatted(to_format):
		"""
		In order to debug easier while programing the project I only worked with space separated bytes as input.
		Example input doesn't have spaces, so it's easier to handle the key with no spaces in order to just copy
		paste the auto-grader input.
		"""
		return to_format if " " in to_format else " ".join(to_format[i:i + 2] for i in range(0, len(to_format), 2))

	@staticmethod
	def print(round_num, legend, hex_string):
		"""
		Matches format from Appendix C for debugging.

		Legend for CIPHER (ENCRYPT) (round number r = 0 to 10, 12 or 14):
			input: cipher input
			start: state at start of round[r]
			s_box: state after SubBytes()
			s_row: state after ShiftRows()
			m_col: state after MixColumns()
			k_sch: key schedule value for round[r]
			output: cipher output

		Legend for INVERSE CIPHER (DECRYPT) (round number r = 0 to 10, 12 or 14):
			iinput: inverse cipher input
			istart: state at start of round[r]
			is_box: state after InvSubBytes()
			is_row: state after InvShiftRows()
			ik_sch: key schedule value for round[r]
			ik_add: state after AddRoundKey()
			ioutput: inverse cipher output
		"""
		print(f'round[{round_num}].{legend}: {hex_string.replace(" ", "")}')
