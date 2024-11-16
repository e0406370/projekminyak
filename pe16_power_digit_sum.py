"""
  Problem 16 - Power Digit Sum
  
  2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
  
  What is the sum of the digits of the number 2^1000 ?
"""


# x^n
def get_power(x: int, n: int) -> int:
  res = 1
  
  while n > 0:
    res *= x
    n -= 1
  
  return res


def get_digits_sum(num: int) -> int:
  res = 0
  
  while num > 0:
    res += num % 10
    num //= 10
    
  return res


x = 2
n = 1000
print(get_power(x, n))
print(get_digits_sum(get_power(x, n)))