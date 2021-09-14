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

		cipher_key = CipherKey(cipher_key)

		schedule = ke.get_schedule(cipher_key)
		state = self.inv_cph.add_round_key(ftr.state_from_str(word), schedule[cipher_key.nr])

		for r in range(cipher_key.nr - 1, 0, -1):  # "r" for "round"
			state = self.inv_cph.mix_columns(self.inv_cph.add_round_key(self.inv_cph.sub_bytes(self.inv_cph.shift_rows(state)), schedule[r]))

		state = self.inv_cph.add_round_key(self.inv_cph.sub_bytes(self.inv_cph.shift_rows(state)), schedule[0])

		return ftr.str_from_state(state)
