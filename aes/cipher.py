from s_box import SBox


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

	"""
	
	"""
	@staticmethod
	def mix_columns(state):

