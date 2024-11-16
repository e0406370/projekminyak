import math, sys


# n is a natural number, i.e. n >= 1
def get_nth_triangular_number(n: int) -> int:
  return int((n / 2) * (1 + n))


# num is a natural number, i.e. num >= 1
def get_divisors(num: int) -> list:
  divisors = [1]
  
  for x in range(2, int(math.sqrt(num)) + 1):
    if num % x == 0:
      divisors.extend([x, int(num / x)])
      
  if num > 1: 
    divisors.append(num)
  
  return sorted(divisors)


def get_answer(divs_size: int, display_all: bool = False) -> int:
  def display(x: int, tri: int, divs: list):
    print(
      f"{x}. Divisors of {tri} [{len(divs)}] -> {' '.join(str(div) for div in divs)}"
    )
  
  for x in range(1, sys.maxsize):
    tri = get_nth_triangular_number(x)
    divs = get_divisors(tri)
    
    if (len(divs) > divs_size):
      display(x, tri, divs)
      break
      
    if display_all:
      display(x, tri, divs)

    
get_answer(5, True)
get_answer(500)