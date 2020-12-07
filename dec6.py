# Write a function called half_xmas_tree(depth) that takes as argument an integer and prints half of a christmas tree of given depth using 1s (for the xmas tree) and 0s (for the background). For example, calling half_xmas_tree(6) one should get the following output:
# [[1, 0, 0, 0, 0, 0],
# [1, 1, 0, 0, 0, 0],
# [1, 1, 1, 0, 0, 0],
# [1, 1, 1, 1, 0, 0],
# [1, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1]]
# If you are able to, write additionally a function called whole_xmas_tree(depth) that prints an entire christmas tree of a given depth :)

import numpy as np

def half_xmas_tree(depth):
  array = np.full((depth, depth), 2)
  print(array)
  return



if __name__ == '__main__':
    length = 6
    half_xmas_tree(length)