from unittest import TestCase
from math import comb
from binomial_coefficients import BinomialCoefficients


class BinomialCofficientsTest(TestCase):

    def test_n_choose_k(self):
        n, k = 4, 3
        for n, k in [(4, 3), (6, 3), (7, 6), (10, 6)]:
            expected = comb(n, k)
            produced = BinomialCoefficients.n_choose_k(n, k)
            print(f" n = {n}, k = {k}, Produced: {produced}, Expected: {expected}")
            self.assertEqual(expected, produced)

    def test_k_larger_than_n(self):
        n, k = 4, 10
        self.assertEqual(BinomialCoefficients.n_choose_k(n, k), 0)
