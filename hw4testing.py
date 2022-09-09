from unittest import TestCase, main
from hw4 import password_validation, withdrawal, balance, account_balance
from hw4 import withdrawal_validation


class TestIfPasswordCorrect(TestCase):
    def test_password(self):
        expected = True
        result = password_validation(password=1989)
        print(result)
        self.assertEqual(expected, result)


class TestMoney(TestCase):
    def test_account_balance(self):
        expected = 100
        result = withdrawal_validation(amount=100)
        print(result)
        self.assertEqual(expected, result)

    def test_withdrawal_amount(self):
        expected = withdrawal
        result = withdrawal_validation(withdrawal<=100)
        print(result)
        self.assertEqual(expected, result)

    def test_raised_value_Error(self):
        if not withdrawal <= account_balance:
            print(balance)
            with self.assertRaises(ValueError):
                withdrawal_validation(balance)









# struggle struggle struggle.













    if __name__ == '__main__':
        main()
