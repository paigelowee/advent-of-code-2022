import os
import sys
# Not working...

sys.setrecursionlimit(1500)

def main():
  soln1()
  # soln2()

def compare(x, y):
  if x == None or y == None:
    return 0
  # If both values are integers, the lower integer should come first.
  # If the left integer is lower than the right integer, the inputs are in the right order.
  #  If the left integer is higher than the right integer, the inputs are not in the right order.
  #  Otherwise, the inputs are the same integer; continue checking the next part of the input.
  if type(x) == type(1) and type(y) == type(1):
    if x < y:
      return 1
    if x > y:
      return -1
    if x == y:
      return 0
  # if either value is an integer convert to an array
  if type(x) != list:
    x = [x]
  if type(y) != list:
    y = [y]
  # If both values are lists, compare the first value of each list, then the second value, and so on.
  same_length = False
  if len(x) == len(y):
    same_length == True

  if len(x) != 0 and len(y) != 0:
    for idx in range(min(len(x), len(y))):

      order =  compare(x[idx], y[idx])
      # if out of order return
      if order == -1:
        return -1
      idx+=1

  # if we get to here no comparison shows out of order:
  # If the left list runs out of items first, the inputs are in the right order.
  # If the right list runs out of items first, the inputs are not in the right order.
  # If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
  if len(x) < len(y):
    return 1
  if len(y) > len(x):
    return -1
  # if len(x) == len(x):
  return 0

def soln1():
  data = []
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    data = [line.replace('\n', '') for line in file]

  pair1 = None
  pair2 = None
  pair_idx = 1
  correct_order = 0
  for line in data:
    # On an empty line we have initialised our pair and need to evalutate it
    if not line:
      order = compare(pair1, pair2)
      if order == 1:
        correct_order +=1

      pair_idx +=1
      pair1 = None
      pair2 = None
      continue

    if not pair1:
      pair1 = eval(line)
      continue

    if not pair2:
      pair2 = eval(line)
      continue




if __name__ == '__main__':
  main()