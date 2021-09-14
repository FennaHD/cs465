from abc import ABC, abstractmethod
from box import Box


class AbstractCipher(ABC):
	"""
	Base class for Cipher and InverseCipher which have common methods.
	Note that the state is always 128 bits (4x4 bytes).
	For consistency, we are interpreting state[x][y] as `x` being COLUMNS and `y` being ROWS.

	For example, if

	A E I M
	B F J N
	C G K O
	D H L P

	is the graphical state, where each letter is an int byte, then the state would be

	[[A, B, C, D]
	[E, F, G, H],
	[I, J, K, L],
	[M, N, O, P]]

	This is completely arbitrary, as some operations are easier vertically and some horizontally (I think)
	"""

	# Override with either an SBox or an InverseSBox
	box: Box

	def sub_bytes(self, state):
		"""
		This function should simply map every byte in the state with the S-box
		and return the new state. The input state is a 4x4 2D byte array.
		"""
		for i in range(4):
			for j in range(4):
				state[i][j] = self.box.transformation(state[i][j])
		return state

	@abstractmethod
	def shift_rows(self, state):
		pass

	@abstractmethod
	def mix_columns(self, state):
		pass

	def add_round_key(self, state, round_key):
		"""
		Given an input state and round_key, XOR state's and round_key's COLUMNS and return the resulting state.

				A' E' I' M'       As Es Is Ms       Ak Ek Ik Mk
				B' F' J' N'   =   Bs Fs Js Ns  xor  Bk Fk Jk Nk
				C' G' K' O'       Cs Gs Ks Os       Ck Gk Kk Ok
				D' H' L' P'       Ds Hs Ls Ps       Dk Hk Lk Pk
				 new_state			 state           round_key

		Column-by-column, as follows:

				A'     As       Ak
				B'  =  Bs  xor  Bk
				C'     Cs       Ck
				D'     Ds       Dk

		"""
		# Combine both arrays into one so that the columns that are supposed to be XORd match.
		zipped = list(zip(state, round_key))
		# Combine the sub arrays so that the bytes that supposed to be XORd match positions.
		zipped_bytes = list(map(lambda a: list(zip(a[0], a[1])), zipped))
		# Now that all bytes are matching, XOR all of them and return the new state
		return list(map(lambda a: list(map(lambda b: b[0] ^ b[1], a)), zipped_bytes))

