#!/usr/bin/python

import sys
import itertools

choices = [['rock'], ['paper'], ['scissors']]

def rock_paper_scissors(num_plays):

  for i in range(0, len(choices)+1):
    for subset in itertools.combinations(choices, i):
      return(subset)
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')