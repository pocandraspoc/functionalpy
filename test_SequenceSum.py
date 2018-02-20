import unittest
import SequenceSum

class Testuntil(unittest.TestCase):

	def test_multi_3_5(self):
		result = SequenceSum.multi_3_5(5)
		self.assertEqual(result, True)
		result_02 = SequenceSum.multi_3_5(9)
		self.assertEqual(result_02, True)

	def test_until(self):
		result = SequenceSum.until(10, SequenceSum.multi_3_5, 3)
		self.assertEqual(result, [3, 5, 6, 9])

if __name__ == '__main__':
	unittest.main()