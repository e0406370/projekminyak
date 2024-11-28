"""
  Problem 14 - Longest Collatz Sequence
  
  The following iterative sequence is defined for the set of positive integers:
    n → n / 2 (if n is even)
    n → 3n + 1 (if n is odd)
  
  Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.
  It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
  
  Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

  Which starting number, under one million, produces the longest chain?
  Note: Once the chain starts, the terms are allowed to go above one million.
"""


# n is starting number of the sequence
def get_collatz_sequence(n: int) -> list:  
  sequence = [n]
  
  while n not in (0, 1):
    if n % 2 == 0:
      n = n // 2
    else:
      n = (3 * n) + 1
      
    sequence.append(n)
  
  return sequence


# skips even numbers since their collatz sequences are always decreasing
def display_longest_collatz_chain(limit: int, display_all = False) -> list:
  sequences = [get_collatz_sequence(i) for i in range(1, limit, 2)]

  if display_all:
    print(
      "\n".join(f"{idx * 2 - 1} ({len(seq)})| {seq}" for idx, seq in enumerate(sequences, start=1))
    )

  sequences.sort(key=lambda x: -len(x))
  longest_sequence = sequences[0]

  print(
    f"\nLongest sequence for limit {limit}:\n{longest_sequence[0]} ({len(longest_sequence)})| {longest_sequence}"
  )


limit = 1000000
display_longest_collatz_chain(limit)