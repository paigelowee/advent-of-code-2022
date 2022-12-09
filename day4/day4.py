import os

def soln1():
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    pairs = 0
    for line in file:
      line = line.replace('\n', '').split(',')
      elf1 = line[0].split('-')
      elf2 = line[1].split('-')
      if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        pairs +=1
      elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        pairs +=1
  print(pairs)

def soln2():
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    pairs = 0
    for line in file:
      line = line.replace('\n', '').split(',')
      elf1 = line[0].split('-')
      elf2 = line[1].split('-')

      if any(x in range(int(elf2[0]), int(elf2[1]) + 1) for x in range(int(elf1[0]), int(elf1[1]) + 1)):
        pairs +=1
      elif any(x in range(int(elf1[0]), int(elf1[1]) + 1) for x in range(int(elf2[0]), int(elf2[1]) + 1)):
        pairs +=1
  print(pairs)

def main():
  soln1()
  soln2()

if __name__ == '__main__':
  main()