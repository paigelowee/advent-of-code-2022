def soln1():
  with open('day7/input.txt', 'r') as file:
    # maintain current path
    path = ['/']
    file_sizes = {}
    for line in file:
      line = line.replace('\n', '')

      # handle commands (directory navigation)
      if line.startswith('$'):
        if ' cd ' in  line:
          directory = line.replace('$ cd', '').replace(' ', '')
          if directory == '/':
            path = ['/']
          elif directory == '..':
            path.pop()
          else:
            path.append(directory)

      # handle directory content
      else:
        if not line.startswith('dir'):
          size = int(line.split(' ')[0])
          current_path = ''
          for directory in path:
            current_path += directory + '/' if directory != '/' else '/'
            file_sizes[current_path] = file_sizes.get(current_path, 0) + size

    total = 0
    for v in file_sizes.values():
      if v < 100000:
        total+=v

    # soln1
    print(total)
    # soln2
    min_space_needed = 70000000 - 30000000
    total_used = file_sizes['/']
    least_removal = 10000000000000
    for v in file_sizes.values():
      if (total_used - v) <= min_space_needed:
        # we can remove it - check if its small
        if v < least_removal:
          least_removal = v
    print(least_removal)

def main():
  soln1()

if __name__ == '__main__':
  main()