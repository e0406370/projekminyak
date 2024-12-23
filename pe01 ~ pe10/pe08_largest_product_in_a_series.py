"""
  Problem 8 - Largest Product in a Series
  
  The four adjacent digits in the 1000-digit number (refer below) that have the greatest product are 9 x 9 x 8 x 9 = 5832
  Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

import re

THOUSAND_DIGITS_STR = """
  73167176531330624919225119674426574742355349194934
  96983520312774506326239578318016984801869478851843
  85861560789112949495459501737958331952853208805511
  12540698747158523863050715693290963295227443043557
  66896648950445244523161731856403098711121722383113
  62229893423380308135336276614282806444486645238749
  30358907296290491560440772390713810515859307960866
  70172427121883998797908792274921901699720888093776
  65727333001053367881220235421809751254540594752243
  52584907711670556013604839586446706324415722155397
  53697817977846174064955149290862569321978468622482
  83972241375657056057490261407972968652414535100474
  82166370484403199890008895243450658541227588666881
  16427171479924442928230863465674813919123162824586
  17866458359124566529476545682848912883142607690042
  24219022671055626321111109370544217506941658960408
  07198403850962455444362981230987879927244284909188
  84580156166097919133875499200524063689912560717606
  05886116467109405077541002256983155200055935729725
  71636269561882670428252483600823257530420752963450
"""


class AdjacentDigitsProduct():
  def __init__(self, product: int, digits: str, initial_pos: int, final_pos: int):
    self.product = product
    self.digits = digits
    self.initial_pos = initial_pos
    self.final_pos = final_pos

  def __str__(self):
    return f"digits: {self.digits}|product: {self.product} at position {self.initial_pos} ~ position {self.final_pos}"


def get_adjacent_digits_prods(n: int):
  digits_str = re.sub(r"\s+", "", THOUSAND_DIGITS_STR) # remove newlines in triple quotes-based string
  digits_len = len(digits_str)  
  prods: list[AdjacentDigitsProduct] = []
  
  left_ptr = 0
  right_ptr = left_ptr + (n - 1)
  
  while (right_ptr < digits_len):
    digits = ""
    prod = 1
    
    for i in range(left_ptr, right_ptr + 1):
      curr_digit = digits_str[i]
      
      digits += curr_digit
      prod *= int(curr_digit)
      
    prods.append(AdjacentDigitsProduct(prod, digits, left_ptr, right_ptr))  
    
    left_ptr += 1
    right_ptr += 1

  # display all combinations of n adjacent digits along with their product and positions
  print("\n".join(str(prod) for prod in prods))
  
  # display the adjacent digits that has the greatest product
  print(f"Answer: {max(prods, key=lambda prod: prod.product)}")


get_adjacent_digits_prods(4)
get_adjacent_digits_prods(13)