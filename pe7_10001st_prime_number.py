"""
  Problem 7 - 10001st Prime
  
  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
  What is the 10001st prime number?
"""

def is_prime(num: int) -> bool:
  if (num < 2):
    return False
  
  LOWER_LIMIT = 2
  UPPER_LIMIT = int(num ** 0.5)
  
  for i in range(LOWER_LIMIT, UPPER_LIMIT + 1, 1):
    if num % i == 0:
      return False
  
  return True 

def get_nth_prime(n: int) -> int:
  num = 2
  ctr = 0
  
  while ctr < n:
    if is_prime(num):
      ctr += 1
      
      if ctr == n:
        return num
    
    num += 1
    
  return -1

print(get_nth_prime(10001))