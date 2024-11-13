"""
  Problem 4 - Largest Palindrome Product
  
  A palindromic number reads the same both ways.
  The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
  
  Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindromic_num(num: int) -> bool:
  num_str = str(num)
  
  left_ptr = 0
  right_ptr = len(num_str) - 1
  
  while (left_ptr < right_ptr):
    if (num_str[left_ptr] != num_str[right_ptr]):
      return False
    
    left_ptr += 1
    right_ptr -= 1
    
  return True

def get_largest_nth_digit_num(digits: int) -> int:
  num = 9
  
  while (digits > 1):
    num = num * 10 + num % 10
    digits -= 1   
    
  return num

def get_largest_palindromic_product(digits: int) -> int:
  num1 = get_largest_nth_digit_num(digits)
  num2 = get_largest_nth_digit_num(digits)
  palindromic_prods = []
  
  for i in range(num1, 10 ** (digits - 1) + 1, -1):
    for j in range(num2, 10 ** (digits - 1) + 1, -1):
      prod = i * j
      
      if (is_palindromic_num(prod) and prod not in palindromic_prods):
        print(f"{i} x {j} = {prod}")
        palindromic_prods.append(prod)
        
        break
  
  palindromic_prods.sort(reverse=True)
  print(palindromic_prods)
  
  return palindromic_prods[0]

print(get_largest_palindromic_product(2))
print(get_largest_palindromic_product(3))