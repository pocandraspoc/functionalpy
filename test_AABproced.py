import unittest
import AABproced

class Testproc(unittest.TestCase):

	def proc(self):
		result = AABproced.proc(1,10)
		self.assertEqual(result, 23)
		result_02 = AABproced.proc(1,20)
		self.assertEqual(result_02, 78)

if __name__ == '__main__':
	unittest.main()