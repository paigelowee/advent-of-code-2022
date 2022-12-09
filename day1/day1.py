import os

def main():
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    elf_snacks = []
    total = 0
    for line in file:
      if line != '\n':
        total+= int(line)
      else:
        elf_snacks.append(total)
        total = 0
  print(max(elf_snacks))
  print(sum(sorted(elf_snacks, reverse=True)[0:3]))

if __name__ == '__main__':
  main()

