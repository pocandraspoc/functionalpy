import unittest
import AABproced
import datetime

class Testproc(unittest.TestCase):

	def test_proc(self):
		result = AABproced.proc(1,10)
		self.assertEqual(result, 23)
		result_02 = AABproced.proc(1,20)
		self.assertEqual(result_02, 78)

if __name__ == '__main__':
	unittest.main()
