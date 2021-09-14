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

		ftr.print(0, self.cph.INPUT, word)

		cipher_key = CipherKey(cipher_key)

		schedule = ke.get_schedule(cipher_key)
		ftr.print(0, self.cph.K_SCH, ftr.str_from_state(schedule[0]))

		state = self.cph.add_round_key(ftr.state_from_str(self.__formatted_word(word)), schedule[0])

		for r in range(1, cipher_key.nr): # "r" for "round"
			ftr.print(r, self.cph.START, ftr.str_from_state(state))

			state = self.cph.sub_bytes(state)
			ftr.print(r, self.cph.S_BOX, ftr.str_from_state(state))

			state = self.cph.shift_rows(state)
			ftr.print(r, self.cph.S_ROW, ftr.str_from_state(state))

			state = self.cph.mix_columns(state)
			ftr.print(r, self.cph.M_COL, ftr.str_from_state(state))

			state = self.cph.add_round_key(state, schedule[r])

			ftr.print(r, self.cph.K_SCH, ftr.str_from_state(schedule[r]))

		state = self.cph.sub_bytes(state)
		ftr.print(cipher_key.nr, self.cph.S_BOX, ftr.str_from_state(state))

		state = self.cph.shift_rows(state)
		ftr.print(cipher_key.nr, self.cph.S_ROW, ftr.str_from_state(state))

		state = self.cph.add_round_key(state, schedule[cipher_key.nr])

		ftr.print(cipher_key.nr, self.cph.K_SCH, ftr.str_from_state(schedule[cipher_key.nr]))

		ftr.print(cipher_key.nr, self.cph.OUTPUT, ftr.str_from_state(state))
		return ftr.str_from_state(state)

	def __formatted_word(self, word):
		"""
		In order to debug easier while programing the project I only worked with space separated bytes as input.
		Example input doesn't have spaces, so it's easier to handle the key with no spaces in order to just copy
		paste the auto-grader input.
		"""
		return word if " " in word else " ".join(word[i:i + 2] for i in range(0, len(word), 2))