from s_box import SBox
from ff_math import FFMath as ffm


class Cipher:
	"""
	The state is always 128 bits (4x4 bytes).
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
	# state = [[]]

	"""
	This function should simply map every byte in the state with the S-box
	and return the new state. The input state is a 4x4 2D byte array.
	"""
	@staticmethod
	def sub_bytes(state):
		sb = SBox()
		for i in range(4):
			for j in range(4):
				state[i][j] = sb.get_transformation(state[i][j])
		return state

	"""
	The bytes in the last three rows of the State are cyclically
	shifted over different numbers of bytes (offsets). The first row, r = 0, is not shifted.

	E.g.

	A E I M           A E I M
	B F J N    -->    F J N B
	C G K O           K O C G
	D H L P           P D H L
	"""
	@staticmethod
	def shift_rows(state):
		# This method would be easier if our state arrangement was horizontal instead of vertical,
		# but since it isn't and we know our state will always be the same size, I believe the easiest way to do this is to hardcode the shifting.
		# Create a temp row or otherwise the bytes will be overridden as we shift.
		new_state = [[state[0][0], state[1][1], state[2][2], state[3][3]],
		             [state[1][0], state[2][1], state[3][2], state[0][3]],
		             [state[2][0], state[3][1], state[0][2], state[1][3]],
		             [state[3][0], state[0][1], state[1][2], state[2][3]]]

		return new_state

	@staticmethod
	def mix_columns(state):
		"""
		Transformation on the state column-by-column.
		Since we are always performing the same operations over different bytes, we will hardcode said operations.
		"""
		for i in range(4):
			col = state[i]
			new_column = [
				ffm.add(ffm.multiply(col[0], 0x02), ffm.multiply(col[1], 0x03), col[2], col[3]),
				ffm.add(col[0], ffm.multiply(col[1], 0x02), ffm.multiply(col[2], 0x03), col[3]),
				ffm.add(col[0], col[1], ffm.multiply(col[2], 0x02), ffm.multiply(col[3], 0x03)),
				ffm.add(ffm.multiply(col[0], 0x03), col[1], col[2], ffm.multiply(col[3], 0x02))
			]
			state[i] = new_column
		return state

	@staticmethod
	def add_round_key(state, round_key):
		"""
		Given an input state and round_key, XOR state and round_key and return the resulting state.

		A' E' I' M'         As Es Is Ms       Ak Ek Ik Mk
		B' F' J' N'    =    Bs Fs Js Ns  xor  Bk Fk Jk Nk
		C' G' K' O'         Cs Gs Ks Os       Ck Gk Kk Ok
		D' H' L' P'         Ds Hs Ls Ps       Dk Hk Lk Pk
		 new_state			   state           round_key
		"""
		# Combine both arrays into one so that the columns that are supposed to be XORd match.
		zipped = list(zip(state, round_key))
		# Combine the sub arrays so that the bytes that supposed to be XORd match positions.
		zipped_bytes = list(map(lambda a: list(zip(a[0], a[1])), zipped))
		# Now that all bytes are matching, XOR all of them and return the new state
		return list(map(lambda a: list(map(lambda b: b[0] ^ b[1], a)), zipped_bytes))

