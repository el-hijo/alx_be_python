import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.Testcase):
    def setUp(self):
        self.calc = SimpleCalculator()
         self.a = 20
         self.b = 10
         self.zero = 0
         
    def test_add(self):
        result = add(self.a, self.b)
        self.assertEqual(result, 30)
    
    def test_subtract(self):
        result = subtract(self.a, self.b)
        self.assertEqual(result, 10)

    def test_multiply(self):
        result = multiply(self.a, self.b)
        self.assertEqual(result, 200)
        
    def test_divide(self):
        result = divide(self.a, self.b)
        self.assertEqual(result, 2)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(self.a, self.zero)          