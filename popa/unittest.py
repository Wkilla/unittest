import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Main(root)

    def test_logicalc(self):
        self.assertEqual(self.calc.logicalc('1'), None)
        self.assertEqual(self.calc.formula, '1')
        self.assertEqual(self.calc.logicalc('+'), None)
        self.assertEqual(self.calc.formula, '1+')
        self.assertEqual(self.calc.logicalc('2'), None)
        self.assertEqual(self.calc.formula, '1+2')
        self.assertEqual(self.calc.logicalc('='), None)
        self.assertEqual(self.calc.formula, '3')
        self.assertEqual(self.calc.logicalc('C'), None)
        self.assertEqual(self.calc.formula, '')

if __name__ == '__main__':
    unittest.main()