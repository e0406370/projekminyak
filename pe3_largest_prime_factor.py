"""
  Problem 3 - Largest Prime Factor
  
  The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600851475143?
"""

import math

def get_prime_factors(num: int) -> list:
  prime_factors = []
  LOWER_LIMIT = 2
  UPPER_LIMIT = int(math.sqrt(num))
  
  for i in range(LOWER_LIMIT, UPPER_LIMIT + 1, 1):
    if (num % i == 0):
      prime_factors.append(i)
      num /= i
  
  if (num > 0):
    prime_factors.append(num)
  
  return prime_factors

print(max(get_prime_factors(600851475143)))