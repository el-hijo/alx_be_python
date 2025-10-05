import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.Testcase):
    def setUp(self):
        self.calc = SimpleCalculator()
         self.a = 20
         self.b = 10
         self.zero = 0
         
    def test_addition(self):
        self.assertEqual(self.calc.add(20, 10), 30)
    
    def test_addition_negative(self):
        self.assertEqual(self.calc.add(-20, 10), -10)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(20, 10), 10)
        
    def test_subtraction_negative(self):
        self.assertEqual(self.calc.subract(-20, 10), -30)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(20, 10), 200)
        
    def test_multiply_negative_a(self):
        self.assertEqual(self.calc.multiply(-20, 10), -200)
    
    def test_multiply_negative_a_b(self):
        self.assertEqual(self.calc.multiply(-20, -10), 200)
    
        
    def test_divide(self):
        result = divide(self.a, self.b)
        self.assertEqual(result, 2)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(self.a, self.zero)          