# -*- coding: utf-8 -*-
"""
This program computes basic statistics
"""

fpath = r'random_nums.txt'

def read_ints(filePath):
    h = open(fpath,'r')
    dats = h.read().split('\n')
    return [int(x) for x in dats]

def count(lst:list) -> int:
    return len(lst)

def summation(nums:list) -> int:
    return sum(nums)

def average(nums:list) -> float:
    return summation(nums) / count(nums)

def minimum(nums:list) -> int:
    return min(nums)

def maximum(nums:list) -> int:
    return max(nums)

def harmonic_mean(nums:list) -> float:
    recips = [1/n for n in nums]
    return count(nums) / summation(recips)

def variance(nums:list) -> float:
    avg = average(nums)
    sqrDiffs = [(float(n)-avg)**2 for n in nums]
    return average(sqrDiffs)

def standard_dev(nums:list) -> float:
    var = variance(nums)
    return var**0.5

if __name__ == '__main__':
    nums = read_ints(fpath)
    print(type(nums))
    print('count: %6d' % count(nums))
    print('summation: %6d' % summation(nums))
    print('average: %5.3f' % average(nums))
    print('minimum: %6d' % minimum(nums))
    print('maximum: %6d' % maximum(nums))
    print('harmonic_mean: %5.3f' % harmonic_mean(nums))
    print('variance %5.3f' % variance(nums))
    print('standard_dev %5.3f' % standard_dev(nums))