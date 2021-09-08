from s_box import SBox
import unittest


class SBoxTest(unittest.TestCase):

	sb = SBox()

	def test_index(self):
		self.assertEqual(0, SBox.get_s_box_index("0"))
		self.assertEqual(7, SBox.get_s_box_index("7"))
		self.assertEqual(10, SBox.get_s_box_index("a"))
		self.assertEqual(15, SBox.get_s_box_index("f"))
		self.assertNotEqual(8, SBox.get_s_box_index("9"))
		self.assertNotEqual(13, SBox.get_s_box_index("c"))

	def test_transformation_top_right_corner(self):
		self.assertEqual(0x76, self.sb.get_transformation(0x0f))
		self.assertNotEqual(0x63, self.sb.get_transformation(0x0f))

	def test_transformation_bot_left_corner(self):
		self.assertEqual(0x8c, self.sb.get_transformation(0xf0))
		self.assertNotEqual(0x16, self.sb.get_transformation(0xf0))

	def test_transformation_top_left_corner(self):
		self.assertEqual(0x63, self.sb.get_transformation(0x00))
		self.assertNotEqual(0x76, self.sb.get_transformation(0x00))
