import unittest
from test import is_prime, calculate_fibonacci, sum_of_primes_in_fibonacci  # Import functions from test.py

class TestFibonacciPrimeFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))  # 2 is prime
        self.assertFalse(is_prime(4))  # 4 is not prime
        self.assertTrue(is_prime(13))  # 13 is prime
        self.assertFalse(is_prime(9))  # 9 is not prime

    def test_calculate_fibonacci(self):
        self.assertEqual(calculate_fibonacci(0), [])  # Fibonacci of 0 terms is []
        self.assertEqual(calculate_fibonacci(1), [0])  # Fibonacci of 1 term is [0]
        self.assertEqual(calculate_fibonacci(5), [0, 1, 1, 2, 3])  # Fibonacci of 5 terms

    def test_sum_of_primes_in_fibonacci(self):
        self.assertEqual(sum_of_primes_in_fibonacci(0), 0)  # No terms, sum is 0
        self.assertEqual(sum_of_primes_in_fibonacci(1), 0)  # No primes in the first term
        self.assertEqual(sum_of_primes_in_fibonacci(5), 5)  # Sum of primes in the first 5 Fibonacci terms [0, 1, 1, 2, 3]

if __name__ == "__main__":
    unittest.main()
