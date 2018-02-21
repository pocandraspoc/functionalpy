import unittest
import sqrt

class Testuntil(unittest.TestCase):

	def test_sqrt(self):
		result = sqrt.sqrt(1, 0.001, 81)
		self.assertAlmostEqual(result, 9, 5)

if __name__ == '__main__':
	unittest.main()