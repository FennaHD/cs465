from ff_math import FFMath as ffm
from r_con import Rcon as rc
from s_box import SBox


class KeyExpansionManager:
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
		byte_array = list(map(lambda w: int(w, 16), cipher_key.split(" ")))
		i = 0
		# TODO remove this later, only temporary
		nk = 4
		w = []
		while i < nk:
			i4 = 4 * i
			w.append(byte_array[i4:i4 + 4])
			i += 1
		return w

	def get_all_words(self, cipher_key):
		"""
		Implements algorithm as shown in 5.2, figure 11.
		@:param cipher_key is a string of space separated hex bytes.
		E.g. "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c".
		"""
		w = self.get_initial_words(cipher_key)

		nk = 4
		nb = 4
		nr = 10

		i = 4
		while i < (nb * (nr + 1)):
			temp = w[i-1]
			if i % 4 == 0:
				temp = ffm.add_words(self.sub_word(self.rot_word(temp)), rc.get(int(i / nk)))
			# else:
			# 	temp = self.sub_word(temp)
			w.append(ffm.add_words(w[i-nk], temp))
			i += 1
		return w

	def get_schedule(self, cipher_key):
		"""
		Returns array of states. Each state is a 4x4 byte array.
		:param cipher_key:
		:return:
		"""
		w = self.get_all_words(cipher_key)
		schedule = []
		for i in range(len(w)):
			word_first_index = i * 4
			schedule.append(w[word_first_index : word_first_index + 4])
		return schedule

	"""
	Takes a four-byte input word and substitutes each byte in that word
	with its appropriate value from the S-Box.
	"""
	@staticmethod
	def sub_word(word):
		# TODO create an instance of SBox at the class level
		return list(map(lambda w: SBox().get_transformation(w), word))

	"""
	Performs a cyclic permutation on its input word.
	[A, B, C, D] becomes [B, C, D, A]
	"""
	@staticmethod
	def rot_word(word):
		return word[1:] + [word[0]]
