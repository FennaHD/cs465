from abstract_cipher import AbstractCipher
from ff_math import FFMath as ffm
from inv_s_box import InverseSBox


class InverseCipher(AbstractCipher):

	box = InverseSBox()

	def shift_rows(self, state):
		"""
		The bytes in the last three rows of the State are cyclically
		shifted over different numbers of bytes (offsets). The first row, r = 0, is not shifted.

		E.g.

		A E I M           A E I M
		B F J N    -->    N B F J
		C G K O           K O C G
		D H L P           H L P D
		"""
		# This method would be easier if our state arrangement was horizontal instead of vertical,
		# but since it isn't and we know our state will always be the same size, I believe the easiest way to do this is to hardcode the shifting.
		# Create a temp state or otherwise the bytes will be overridden as we shift.
		new_state = [[state[0][0], state[3][1], state[2][2], state[1][3]],
		             [state[1][0], state[0][1], state[3][2], state[2][3]],
		             [state[2][0], state[1][1], state[0][2], state[3][3]],
		             [state[3][0], state[2][1], state[1][2], state[0][3]]]

		return new_state

	def mix_columns(self, state):
		"""
		Transformation on the state column-by-column.
		Since we are always performing the same operations over different bytes, we will hardcode said operations.
		"""
		for i in range(4):
			col = state[i]
			new_column = [
				ffm.add_bytes(ffm.multiply(col[0], 0x0e), ffm.multiply(col[1], 0x0b), ffm.multiply(col[2], 0x0d), ffm.multiply(col[3], 0x09)),
				ffm.add_bytes(ffm.multiply(col[0], 0x09), ffm.multiply(col[1], 0x0e), ffm.multiply(col[2], 0x0b), ffm.multiply(col[3], 0x0d)),
				ffm.add_bytes(ffm.multiply(col[0], 0x0d), ffm.multiply(col[1], 0x09), ffm.multiply(col[2], 0x0e), ffm.multiply(col[3], 0x0b)),
				ffm.add_bytes(ffm.multiply(col[0], 0x0b), ffm.multiply(col[1], 0x0d), ffm.multiply(col[2], 0x09), ffm.multiply(col[3], 0x0e)),
			]
			state[i] = new_column
		return state
