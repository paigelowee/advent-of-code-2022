import math
import os

def main():
  soln1()
  soln2()

def soln1():
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    visible_count = 0
    data = [list(line.replace('\n', '')) for line in file]
    end_col = len(data[0]) -1
    end_row = len(data) -1

    # a flipped array of the data so we can compare above and below each tree in an array
    column_array = [[] for _ in range(end_row + 1)]
    for row_index, row in enumerate(data):
      for y_index, col in enumerate(row):
        column_array[y_index].append(col)

    for row_index, row in enumerate(data):
      for y_index, tree in enumerate(row):
        # if at outer section, the tree is visible
        if y_index == 0 or y_index == end_col or row_index == 0 or row_index == end_row:
          visible_count +=1
          continue

        # check left and right of tree for taller tree, if there is none, tree is visible, continue to next tree
        if not( max(row[y_index +1:]) >= tree):
          visible_count +=1
          continue
        if not (max(row[0: y_index]) >= tree):
          visible_count +=1
          continue
        # otherwise we want to check all above, below
        if not(max(column_array[y_index][row_index +1:]) >= tree):
          visible_count +=1
          continue
        if not (max(column_array[y_index][0: row_index]) >= tree):
          visible_count +=1
          continue
    # print(visible_count)

def get_scenic_score(tree, arr, reverse=False):
  scenic_score = 0
  if reverse:
    arr.reverse()
  for x in arr:
    # if tree not blocking view
    if tree > x:
      scenic_score +=1
    elif x >= tree:
      scenic_score +=1
      return int(scenic_score)
  return int(scenic_score)

def soln2():
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    data = [list(line.replace('\n', '')) for line in file]
    end_row = len(data)

    # a flipped array of the data so we can compare above and below each tree in an array
    column_array = [[] for _ in range(end_row)]
    for row_index, row in enumerate(data):
      for y_index, col in enumerate(row):
        column_array[y_index].append(col)

    highest_scenic_score = 0
    for row_index, row in enumerate(data):
      for y_index, tree in enumerate(row):
        right = row[y_index +1:]
        left = row[0: y_index]
        bottom = column_array[y_index][row_index + 1:]
        top = column_array[y_index][0: row_index]
        scenic_scores = []
        for arr in [left, top]:
          s = get_scenic_score(tree, arr, True)
          scenic_scores.append(s)
        for arr in [right, bottom]:
          s = get_scenic_score(tree, arr)
          scenic_scores.append(s)
        scenic_score = math.prod(scenic_scores)
        if scenic_score > highest_scenic_score:
          highest_scenic_score = scenic_score

    print(highest_scenic_score)

if __name__ == '__main__':
  main()