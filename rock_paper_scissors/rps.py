#!/usr/bin/python

import sys
import itertools
from itertools import combinations, product, permutations, combinations_with_replacement

choices = ['rock', 'paper', 'scissors']
# all_combos = [[]]

def rock_paper_scissors(n):
  # all_combos = []
  combos = []
  if n == 0:
    return [[]]
  elif n == 1:
    return [['rock'], ['paper'], ['scissors']]
  else:
    combos.append(list(itertools.product(['rock', 'paper', 'scissors'], repeat=n)))
      
    # all_combos = itertools.product(['rock', 'paper', 'scissors'], repeat=n)
    # all_combos = itertools.product(choices, repeat=n)
    return(combos)
    
    # for _ in range(n, len(choices)+1):
    
    # all_combos = list(combinations_with_replacement(choices, n))
    # # print(len(all_combos), all_combos)
    # return all_combos
  

#
print (rock_paper_scissors(2))
      
# print(rock_paper_scissors(2))

# combos = []
# combos.append(list(itertools.product(['rock', 'paper', 'scissors'], repeat=3)))
# print(combos)



  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    n = int(sys.argv[1])
    print(rock_paper_scissors(n))
  else:
    print('Usage: rps.py [n]')