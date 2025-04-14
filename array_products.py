"""Calculates the product of all elements in a list except the element at the current index.

Args:
    nums: A list of integers.

Returns:
    A list where each element is the product of all elements in nums except the element at the current index."""
from typing import List

def calculate_products(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    # Calculate prefix products
    prefix_prod = 1
    for i in range(n):
        result[i] = prefix_prod
        prefix_prod *= nums[i]

    # Calculate suffix products and multiply with prefix products
    postfix_prod = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix_prod
        postfix_prod *= nums[i]

    return result

# Example usage
nums = [1, 2, 3, 4]
products = calculate_products(nums)
print(products)  # Output: [24, 12, 8, 6]

nums = [0, 1, 2, 3]
products = calculate_products(nums)
print(products) # Output: [6, 0, 0, 0]
