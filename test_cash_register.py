import unittest
from cash_register import Register


class TestCashRegister(unittest.TestCase):

    def test_cash_register(self):
        self.assertEqual(Register.cash_register(0.01, 100), {'£50': 1, '£20': 2, '£5': 1, '£1': 4, '50p': 1, '20p': 2,
                                                           '5p': 1, '1p': 4})

    def test_cash_register2(self):
        self.assertEqual(Register.cash_register2(0.01, 100), {'£50': 1, '£20': 2, '£5': 1, '£1': 4, '50p': 1, '20p': 2,
                                                           '5p': 1, '1p': 4})

    if __name__ == '__main__':
        unittest.main()
