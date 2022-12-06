def main():
    def soln1():
      with open('day5/input.txt') as file:
        data = file.read().split('\n\n')
        moves_data =  data[1]
        stack_data =  data[0]

        # process stack data into 9 lists
        stacks = [[] for _ in range(10)]
        for line in stack_data.split('\n'):
          for x in range(10):
            cargo = line[x*4-4:x*4]
            if '[' in cargo:
              stacks[x-1].append(cargo)

        # reverse the stacks
        stacks = [l[::-1] for l in stacks]

        # process moves
        for line in moves_data.split('\n'):
          line = line.rstrip()
          # convert moves to list of integers
          move = [int(i) for i in line.replace('move', '').replace('from', ',').replace('to', ',').replace(' ', '').split(',')]
          # handle move
          for x in range(move[0]):
            cargo  = stacks[move[1]-1].pop()
            stacks[move[2] -1].append(cargo)

        print(stacks)

    def soln2():
      with open('day5/input.txt') as file:
        data = file.read().split('\n\n')
        moves_data =  data[1]
        stack_data =  data[0]

        # process stack data into 9 lists
        stacks = [[] for _ in range(10)]
        for line in stack_data.split('\n'):
          for x in range(10):
            cargo = line[x*4-4:x*4]
            if '[' in cargo:
              stacks[x-1].append(cargo)

        # reverse the stacks
        stacks = [l[::-1] for l in stacks]

        # process moves
        for line in moves_data.split('\n'):
          line = line.rstrip()
          # convert moves to list of integers
          move = [int(i) for i in line.replace('move', '').replace('from', ',').replace('to', ',').replace(' ', '').split(',')]
          # handle move
          cargo_list = []
          for x in range(move[0]):
            cargo_list.append(stacks[move[1]-1].pop())

          stacks[move[2] -1].extend(cargo_list[::-1])

        print(stacks)

    soln1()
    soln2()

if __name__ == '__main__':
  main()