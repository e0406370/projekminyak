# Problem 1 - Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# standard for loop
def method1(num : int) :
  sum = 0
  
  for i in range(num) :
    if (i % 3 == 0 or i % 5 == 0):
      sum += i
  
  return sum

# generator expression
def method2(num : int) :
  return sum(x for x in range(num) if x % 3 == 0 or x % 5 == 0)

print(method1(1000))
print(method2(1000))