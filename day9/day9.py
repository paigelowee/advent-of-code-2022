import os

def main():
  soln1()
  # soln2()

def soln1():
  data = []
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    data = [line.replace('\n', '') for line in file]

  max_move = max([(int(line.split(' ')[1])) for line in data])

  visited = set()

  hx = max_move -1
  hy = 0

  tx = max_move -1
  ty = 0

  for line in data:
    action = line.split(' ')[0]
    move = int(line.split(' ')[1])

    # move head
    if action == 'U':
      hx -= move
    elif action == 'D':
      hx += move
    elif action == 'L':
      hy -= move
    elif action == 'R':
      hy+= move

    # check if head is 2 steps away
    if abs(hx - tx) == 2:
      increment = 1 if abs(hx - tx) > 0 else -1
      tx += increment

    elif abs(hy - ty) == 2:
      increment = 1 if abs(hy - ty) > 0 else -1
      ty += increment

    # elif
    visited.add((tx, ty))
    print(visited)

    # move tail


if __name__ == '__main__':
  main()