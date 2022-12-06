import string

lower_score_dict = {letter: i + 1 for i, letter in enumerate(string.ascii_lowercase)}
upper_score_dict = {letter: i + 27 for i, letter in enumerate(string.ascii_uppercase)}

def soln1():
  with open('day3/input.txt') as file:
    total = 0
    for line in file:
      line = line.replace("\n", "")
      half_point = round(((len(line)) / 2 ))
      # split the line into halves
      r1 = set(line[0: half_point])
      r2 = set(line[half_point:])
      # find intersect for duplicate value
      intersect = list(r1.intersection(r2))[0]
      # convert intersect character to value
      if intersect[0].isupper():
        value = upper_score_dict[intersect]
      else:
        value = lower_score_dict[intersect]
      total += value
  print(total)

def soln2():
  with open('day3/input.txt') as file:
    input_lines = [line.replace('\n', '') for line in file]
    N = 0
    total = 0
    num_lines = len(input_lines)
    while N < num_lines:
      lines = input_lines[N: N+3]
      line_set = [set(l) for l in lines]
      intersect = list(line_set[0].intersection(line_set[1]).intersection(line_set[2]))[0]
      N+=3
      if intersect.isupper():
        value = upper_score_dict[intersect]
      else:
        value = lower_score_dict[intersect]
      total += value
    print(total)

if __name__ == '__main__':
  soln2()