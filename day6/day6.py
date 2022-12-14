import os

def main():
  soln1()
  soln2()

def soln1():
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    chars = file.readlines()[0]
    for idx, char in enumerate(chars):
      if idx < 4: continue
      subs = chars[idx-4: idx]
      #  if set equals 4, then no duplicate is found
      if len(set(subs)) == 4:
        print(idx)
        break

def soln2():
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    chars = file.readlines()[0]
    for idx, char in enumerate(chars):
      if idx < 14: continue
      subs = chars[idx-14: idx]
      #  if length of set equals 14, then no duplicate is found
      if len(set(subs)) == 14:
        print(idx)
        break

if __name__ == '__main__':
  main()