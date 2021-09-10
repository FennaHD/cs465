from r_con import Rcon as rc
import unittest


class RconTest(unittest.TestCase):

	def test_positive(self):
		self.assertEqual([0x80, 0x00, 0x00, 0x00], rc.get(8))

	def test_negative(self):
		self.assertNotEqual([0x80, 0x00, 0x00, 0x00], rc.get(9))
