from cipher_key import CipherKey
from formatter import Formatter as ftr
from inv_cipher import InverseCipher
from key_expander import KeyExpander as ke


class Decrypter:
	"""
	Runs all necessary operations and algorithms necessary to AES decrypt
	"""

	inv_cph = InverseCipher()

	def decrypt(self, word, cipher_key):

		ftr.print(0, self.inv_cph.INPUT, word)

		cipher_key = CipherKey(cipher_key)

		schedule = ke.get_schedule(cipher_key)
		ftr.print(0, self.inv_cph.K_SCH, ftr.str_from_state(schedule[cipher_key.nr]))

		state = self.inv_cph.add_round_key(ftr.state_from_str(word), schedule[cipher_key.nr])

		i = 1
		for r in range(cipher_key.nr - 1, 0, -1):  # "r" for "round"
			ftr.print(i, self.inv_cph.START, ftr.str_from_state(state))

			state = self.inv_cph.shift_rows(state)
			ftr.print(i, self.inv_cph.S_ROW, ftr.str_from_state(state))

			state = self.inv_cph.sub_bytes(state)
			ftr.print(i, self.inv_cph.S_BOX, ftr.str_from_state(state))

			ftr.print(i, self.inv_cph.K_SCH, ftr.str_from_state(schedule[r]))

			state = self.inv_cph.add_round_key(state, schedule[r])
			ftr.print(i, self.inv_cph.K_ADD, ftr.str_from_state(state))

			state = self.inv_cph.mix_columns(state)

			i = i + 1

		ftr.print(cipher_key.nr, self.inv_cph.START, ftr.str_from_state(state))

		state = self.inv_cph.shift_rows(state)
		ftr.print(cipher_key.nr, self.inv_cph.S_ROW, ftr.str_from_state(state))

		state = self.inv_cph.sub_bytes(state)
		ftr.print(cipher_key.nr, self.inv_cph.S_BOX, ftr.str_from_state(state))

		ftr.print(cipher_key.nr, self.inv_cph.S_ROW, ftr.str_from_state(schedule[0]))

		state = self.inv_cph.add_round_key(state, schedule[0])
		ftr.print(cipher_key.nr, self.inv_cph.OUTPUT, ftr.str_from_state(state))

		return ftr.str_from_state(state)
