# -*- coding: utf-8 -*-
"""
Tests for compute_stats_refactor.py

@author: Sale
"""

import compute_stats_refactor as csr
import unittest

class test_compute_stats(unittest.TestCase):
    def get_random_numbers(self):
        fpath = r'%s\%s' \
            % (r'C:\Users\Sale\Documents\Coursera\TDD\TDD Labs', \
                'random_nums.txt')
        return csr.read_ints(fpath)
    def test_compute_stats_read_ints_reads_file_returns_int_list(self):
        nums = self.get_random_numbers()
        self.assertEqual(len(nums), 1000)
    def test_compute_stats_count_returns_total_number_of_ints(self):
        nums = self.get_random_numbers()
        self.assertEqual(csr.count(nums), 1000)
    def test_compute_stats_summation_returns_sum_of_ints(self):
        nums = self.get_random_numbers()
        self.assertEqual(csr.summation(nums), 499498)
    def test_compute_stats_average_returns_expected(self):
        nums = self.get_random_numbers()
        self.assertEqual(csr.average(nums), 499.498)
    def test_compute_stats_minimum_returns_expected(self):
        nums = self.get_random_numbers()
        self.assertEqual(csr.minimum(nums), 1)
    def test_compute_stats_maximum_returns_expected(self):
        nums = self.get_random_numbers()
        self.assertEqual(csr.maximum(nums), 997)
    def test_compute_stats_harmonic_mean_returns_expected(self):
        nums = self.get_random_numbers()
        self.assertEqual(round(csr.harmonic_mean(nums),3), 129.728)
    def test_compute_stats_variance_returns_expected(self):
        nums = self.get_random_numbers()
        self.assertEqual(round(csr.variance(nums),3), 81476.494)
    def test_compute_stats_standard_dev_returns_expected(self):
        nums = self.get_random_numbers()
        self.assertEqual(round(csr.standard_dev(nums),3), 285.441)
        
if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
    