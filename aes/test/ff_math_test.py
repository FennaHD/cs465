from ff_math import FFMath as ffm
import unittest


class FFMathTest(unittest.TestCase):

	def test_simple_ff_add_positive(self):
		self.assertEqual(0xd4, ffm.add(0x57, 0x83))

	def test_simple_ff_add_negative(self):
		self.assertNotEqual(0xd3, ffm.add(0x57, 0x83))

	def test_nested_ff_add_positive(self):
		self.assertEqual(0xfe, ffm.add(0x57, ffm.add(0xae, 0x07)))

	def test_nested_ff_add_negative(self):
		self.assertNotEqual(0xff, ffm.add(0x57, ffm.add(0xae, 0x07)))

	def test_x_time_no_overflow_positive(self):
		self.assertEqual(0xae, ffm.x_time(0x57))
		self.assertEqual(0x8e, ffm.x_time(0x47))

	def test_x_time_no_overflow_negative(self):
		self.assertNotEqual(0xaf, ffm.x_time(0x57))
		self.assertNotEqual(0x8d, ffm.x_time(0x47))

	def test_x_time_overflow_positive(self):
		self.assertEqual(0x47, ffm.x_time(0xae))
		self.assertEqual(0x07, ffm.x_time(0x8e))

	def test_x_time_overflow_negative(self):
		self.assertNotEqual(0x48, ffm.x_time(0xae))
		self.assertNotEqual(0x06, ffm.x_time(0x8e))

	def test_dict_positive(self):
		self.assertEqual(0xae, ffm.get_x_time_dict(0x57)[1])
		self.assertEqual(0x47, ffm.get_x_time_dict(0x57)[2])
		self.assertEqual(0x8e, ffm.get_x_time_dict(0x57)[3])
		self.assertEqual(0x07, ffm.get_x_time_dict(0x57)[4])

	def test_dict_negative(self):
		self.assertNotEqual(0xad, ffm.get_x_time_dict(0x57)[1])
		self.assertNotEqual(0x48, ffm.get_x_time_dict(0x57)[2])
		self.assertNotEqual(0x8d, ffm.get_x_time_dict(0x57)[3])
		self.assertNotEqual(0x08, ffm.get_x_time_dict(0x57)[4])

	def test_intermediate_results_positive(self):
		self.assertEqual({0x57, 0xae, 0x07}, set(ffm.get_intermediate_results(0x57, 0x13)))

	def test_intermediate_results_negative(self):
		# using a set because tests that return arrays can fail if order is wrong,
		# even if it contains all the correct elements.
		self.assertNotEqual({0xaa, 0x69}, set(ffm.get_intermediate_results(0x57, 0x13)))

	def test_multiply_positive(self):
		self.assertEqual(0xfe, ffm.multiply(0x57, 0x13))

	def test_multiply_negative(self):
		self.assertNotEqual(0xaf, ffm.multiply(0x57, 0x13))

	def test_another_simple_multiply(self):
		self.assertEqual(0xc7, ffm.multiply(0x22, 0x0e))

	def test_complex_multiply_positive(self):
		self.assertEqual(0xc9, ffm.multiply(0x70, 0x27))
		# Test would previously fail if I reversed the order of the arguments.
		# Keep this assertion to make sure we aren't reverting to this bug.
		self.assertEqual(0xc9, ffm.multiply(0x27, 0x70))


if __name__ == '__main__':
	unittest.main()
