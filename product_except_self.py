# Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums
# except nums[I].
# The product of any prefix or suffix of nums is guaranteed to fit in a
# 32-bit integer.
# You must write an algorithm that runs in O(n) time and without
# using the division operation.


import random
from time_finder import calculate_execution_time


@calculate_execution_time
def product_of_array_except_self(nums):
    n = len(nums)
    
    # Create an answer array with the same length as nums
    answer = [0] * n
    
    # Calculate the prefix products
    prefix_products = [1] * n
    for i in range(1, n):
        prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
    
    # Calculate the suffix products
    suffix_products = [1] * n
    for i in range(n - 2, -1, -1):
        suffix_products[i] = suffix_products[i + 1] * nums[i + 1]
    
    # Calculate the answer using prefix and suffix products
    for i in range(n):
        answer[i] = prefix_products[i] * suffix_products[i]
    
    return answer


print(product_of_array_except_self([5, 2, 3, 4]))