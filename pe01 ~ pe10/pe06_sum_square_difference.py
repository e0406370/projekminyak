"""
  Problem 6 - Sum Square Difference
  
  The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
 
  The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
  
  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
  
  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


# (1^2 + 2^2 + ... + n^2)
def get_sum_of_squares(n: int) -> int:
  return (n * (n + 1) * (2 * n + 1)) // 6


# (1 + 2 + ... + n)^2
def get_square_of_sum(n: int) -> int:
  return ((n // 2) * (1 + n)) ** 2


n = 10
print(get_square_of_sum(n) - get_sum_of_squares(n))

n = 100
print(get_square_of_sum(n) - get_sum_of_squares(n))