import os

def main():
  # soln1()
  soln2()

def handle_valid_cycle(cycle, x):
  valid_cycles = [20, 60, 100, 140, 180, 220]
  if cycle in valid_cycles:
    return (cycle * (x))
  return 0

def soln1():
  data = []
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    data = [line.replace('\n', '') for line in file]

  total_x_count = 0
  x = 1
  cycle_count = 1
  for cycle in range(len(data)):
    action = data[cycle]
    # increment by 1, check for valid cycle
    if action == 'noop':
      cycle_count +=1
      total_x_count +=handle_valid_cycle(cycle_count, x)

    # where is x?

    # handle action
    if action != 'noop':
      cycle_count +=1
      total_x_count +=handle_valid_cycle(cycle_count, x)
      x_increment = int(action.split(' ')[1])
      x+= x_increment
      cycle_count +=1
      total_x_count +=handle_valid_cycle(cycle_count, x)


  print(total_x_count)

def soln2():
  data = []
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    data = [line.replace('\n', '') for line in file]

  total_x_count = 0
  x = 1
  x_values = []
  for cycle in range(len(data)):
    action = data[cycle]
    # increment by 1, check for valid cycle
    if action == 'noop':
      x_values.append(x)

    # handle action
    if action != 'noop':
      x_values.append(x)
      x_increment = int(action.split(' ')[1])
      x+= x_increment
      x_values.append(x)

  print(x_values)
  # print(total_x_count)
  output = [[] * 40 for _ in range(6)]

  # we know x position for each cycle point, now loop over clock cycles and print the hashes
  count = 0
  for row in range(0, 6):
    for col in range(0, 40):
      print(count)
      x = x_values[count]
      print(x)
      if count == x or count + 1 == x or count - 1 == x:
        output[row].append('#')
      else:
        output[row].append('.')
      count +=1

  for row in output:
    print(''.join(row))


if __name__ == '__main__':
  main()