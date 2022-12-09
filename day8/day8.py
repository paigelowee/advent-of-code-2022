def main():
  def soln1():
    with open('day8/input.txt', 'r') as file:
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
          # otherwise we want to check all above, belowee):
            visible_count +=1
            continue
          if not (max(column_array[y_index][0: row_index]) >= tree):
            visible_count +=1
            continue

      print(visible_count)
  soln1()

if __name__ == '__main__':
  main()