"""
  Problem 2 - Even Fibonacci Numbers
  
  Each new term in the Fibonacci sequence is generated by adding the previous two terms.
  By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
  By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def fibonacci(n: int, fibonacci_cache: map) -> int:

  # F(0) = 0, F(1) = 1
  if n <= 1: 
    return n
  
  if n in fibonacci_cache:
    return fibonacci_cache[n]
  
  # F(n) = F(n - 1) + F(n - 2)
  fibonacci_cache[n] = fibonacci(n - 1, fibonacci_cache) + fibonacci(n - 2, fibonacci_cache)
  
  return fibonacci_cache[n]

def generate_even_fibonacci_sum(limit: int) -> int:
  
  n = 0
  fibonacci_cache = {}
  fibonacci_even_sum = 0
  
  fibonacci_num = fibonacci(n, fibonacci_cache)
  while (fibonacci_num < limit):
    
    if (fibonacci_num % 2 == 0):
      fibonacci_even_sum += fibonacci_num

    n += 1
    fibonacci_num = fibonacci(n, fibonacci_cache)
      
  return fibonacci_even_sum 

print(generate_even_fibonacci_sum(4000000)) 