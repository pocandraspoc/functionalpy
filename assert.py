#assert.py
import unittest
import datetime

class TestType(unittest.TestCase):

  def test_Int(self):
      a = 1
      self.assertTrue(type(a) is int)
      self.assertIs(type(a), int)
      self.assertIsInstance(a, int)

  def test_Sting(self):
	  a = "hello"
	  self.assertTrue(type(a) is str)
	  self.assertIs(type(a), str)
	  self.assertIsInstance(a, str)
	
  def test_DateTime(self):
  	  a = datetime.date(2012,10,1)
  	  self.assertTrue(type(a) is type(datetime.date(2012,10,1)))

  	
if __name__ == "__main__":
	unittest.main()