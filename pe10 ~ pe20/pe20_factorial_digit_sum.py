"""
  Problem 20 - Factorial Digit Sum
  
  n! means n x (n - 1) x ⋯ x 3 x 2 x 1.

  For example, 10! = 10 x 9 x ⋯ x 3 x 2 x 1 = 3628800,  
  and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

  Find the sum of the digits in the number 100!.
"""


def get_factorial(n: int) -> int:
  if n == 1:
    return 1
  
  return n * get_factorial(n - 1)


def get_digits_sum(num: int) -> int:
  res = 0
  
  while num > 0:
    res += num % 10
    num //= 10
    
  return res


n = 100
print(get_factorial(100))
print(get_digits_sum(get_factorial(n)))