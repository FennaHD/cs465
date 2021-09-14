from cipher import Cipher
from cipher_key import CipherKey
from formatter import Formatter as ftr
from key_expander import KeyExpander as ke

class Encryptor:
	"""
	Runs all necessary operations and algorithms necessary to AES encrypt
	"""

	cph = Cipher()

	def encrypt(self, word, cipher_key):

		cipher_key = CipherKey(cipher_key)

		schedule = ke.get_schedule(cipher_key)
		state = self.cph.add_round_key(ftr.state_from_str(self.__formatted_word(word)), schedule[0])

		for r in range(cipher_key.nr - 1): # "r" for "round"
			state = self.cph.add_round_key(self.cph.mix_columns(self.cph.shift_rows(self.cph.sub_bytes(state))), schedule[r + 1])

		state = self.cph.add_round_key(self.cph.shift_rows(self.cph.sub_bytes(state)), schedule[cipher_key.nr])

		return ftr.str_from_state(state)

	def __formatted_word(self, word):
		"""
		In order to debug easier while programing the project I only worked with space separated bytes as input.
		Example input doesn't have spaces, so it's easier to handle the key with no spaces in order to just copy
		paste the auto-grader input.
		"""
		return word if " " in word else " ".join(word[i:i + 2] for i in range(0, len(word), 2))