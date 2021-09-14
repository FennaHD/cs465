from s_box import SBox
import unittest


class BoxTest(unittest.TestCase):
	"""
	We are using an SBox instance to test the Box methods,
	but should satisfy unit-testing both Box implementations.
	"""

	sb = SBox()

	def test_transformation_top_right_corner(self):
		self.assertEqual(0x76, self.sb.transformation(0x0f))
		self.assertNotEqual(0x63, self.sb.transformation(0x0f))

	def test_transformation_bot_left_corner(self):
		self.assertEqual(0x8c, self.sb.transformation(0xf0))
		self.assertNotEqual(0x16, self.sb.transformation(0xf0))

	def test_transformation_top_left_corner(self):
		self.assertEqual(0x63, self.sb.transformation(0x00))
		self.assertNotEqual(0x76, self.sb.transformation(0x00))
