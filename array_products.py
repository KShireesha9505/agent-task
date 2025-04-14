"""Calculates the product of all elements in a list except the element at the current index.

    Args:
        nums: A list of integers.

    Returns:
        A list where each element is the product of all elements in nums except the element at the current index.

    Examples:
        calculate_products([1, 2, 3, 4]) == [24, 12, 8, 6]
        calculate_products([0, 1, 2]) == [2, 0, 0]
        calculate_products([1, 2, 0, 4]) == [0, 0, 8, 0]
"""
from typing import List

def calculate_products(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    prefix_product = 1
    for i in range(n):
        result[i] = prefix_product
        prefix_product *= nums[i]

    postfix_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix_product
        postfix_product *= nums[i]

    return result