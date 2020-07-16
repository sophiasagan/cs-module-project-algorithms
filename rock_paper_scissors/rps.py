#!/usr/bin/python

import sys
import itertools
from itertools import combinations, product, permutations, combinations_with_replacement

choices = [['rock'], ['paper'], ['scissors']]
# all_combos = [[]]

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  elif n == 1:
    return choices
  else:
    all_combos = itertools.product(choices, repeat=n)
    return list(all_combos)
    
    # for _ in range(n, len(choices)+1):
    
    # all_combos = list(combinations_with_replacement(choices, n))
    # # print(len(all_combos), all_combos)
    # return all_combos
  # for i in range(0, len(choices)+1):
  #   for subset in itertools.combinations(choices, i):
  #     return(subset)
  
print(rock_paper_scissors(2))



  

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     n = int(sys.argv[1])
#     print(rock_paper_scissors(n))
#   else:
#     print('Usage: rps.py [n]')