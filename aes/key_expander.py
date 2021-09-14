from ff_math import FFMath as ffm
from r_con import Rcon as rc
from s_box import SBox


class KeyExpander:
	"""
	Class in charge of performing all operations involving key expansion.
	Is also in charge of transforming input into the format we want to work with.
	So far we are inputting a string of space separated bytes, and we convert the
	substring bytes into hex integers.
	"""

	@staticmethod
	def get_initial_words(cipher_key):
		"""
		Splits key into an array of words, while also reformatting them to be hex integers.
		cipher_key is expected to be a single-space separated string of bytes. E.g.
		"2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c". We can't work with this key, so
		we must first convert it to a format we can use. We decided on a 2D array so that
		with the input from above:

		2b 28 ab 09       [[0x2b, 0x7e, 0x15, 0x16],
		7e ae f7 cf  -->   [0x28, 0xae, 0xd2, 0xa6],
		15 d2 15 4f        [0xab, 0xf7, 0x15, 0x88],
		16 a6 88 3c        [0x09, 0xcf, 0x4f, 0x3c]]

		"""
		# turn "<nibble><nibble>" into int 0x<nibble><nibble>
		byte_array = list(map(lambda w: int(w, 16), cipher_key.key.split(" ")))
		i = 0
		w = []
		while i < cipher_key.nk:
			i4 = 4 * i
			w.append(byte_array[i4:i4 + 4])
			i += 1
		return w

	@staticmethod
	def get_all_words(cipher_key):
		"""
		Implements algorithm as shown in 5.2, figure 11.
		@:param cipher_key is a string of space separated hex bytes.
		E.g. "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c".
		"""
		w = KeyExpander.get_initial_words(cipher_key)

		i = cipher_key.nk
		while i < (cipher_key.nb * (cipher_key.nr + 1)):
			temp = w[i-1]
			if i % cipher_key.nk == 0:
				temp = ffm.add_words(KeyExpander.sub_word(KeyExpander.rot_word(temp)), rc.get(int(i / cipher_key.nk)))
			elif cipher_key.nk > 6 and i % cipher_key.nk == 4:
				temp = KeyExpander.sub_word(temp)
			w.append(ffm.add_words(w[i-cipher_key.nk], temp))
			i += 1
		return w

	@staticmethod
	def get_schedule(cipher_key):
		"""
		Returns array of states. Each state is a 4x4 byte 2D array.
		"""
		num_bytes_in_word = 4
		w = KeyExpander.get_all_words(cipher_key)
		schedule = []
		for i in range(int(len(w)/num_bytes_in_word)):
			word_first_index = i * num_bytes_in_word
			schedule.append(w[word_first_index : word_first_index + num_bytes_in_word])
		return schedule

	@staticmethod
	def sub_word(word):
		"""
		Takes a four-byte input word and substitutes each byte in that word
		with its appropriate value from the S-Box.
		"""
		return list(map(lambda w: SBox().transformation(w), word))

	@staticmethod
	def rot_word(word):
		"""
		Performs a cyclic permutation on its input word.
		[A, B, C, D] becomes [B, C, D, A]
		"""
		return word[1:] + [word[0]]
