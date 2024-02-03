import unittest
class TestCalculator(unittest.TestCase):

  def test_add(self):
    self.assertEqual(self.calculator.add(4,6), 11)
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(10,5), 5)
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(3,7), 21)

if __name__ == "main":
    unittest.main()




