def main():
  def soln1():
    with open('day7/input.txt', 'r') as file:
      # maintain current path
      file_struct = {}
      file_sizes = {}
      curr_file = '/'
      for line in file:
        line = line.replace('\n', '')

        # handle commands (directory navigation)
        if line.startswith('$'):
          if ' cd ' in  line:
            directory = line.replace('$ cd', '').replace(' ', '')
            curr_file = directory

        # handle directory content
        else:
          # add to curr dir size
          if curr_file not in file_sizes:
            file_sizes[curr_file] = 0
          if curr_file not in file_struct:
            file_struct[curr_file] = []
          if not line.startswith('dir'):
            size = int(line.split(' ')[0])
            file_sizes[curr_file] += size
          else:
            dir = line.split(' ')[1]
            file_sizes
            file_struct[curr_file].append(dir)
      total_size = 0

      for k, v in file_struct.items():
        dir_size = get_file_size(k, file_sizes, file_struct)

        if dir_size <= 100000:
          total_size += dir_size

      print(total_size)

  def get_file_size(key, file_sizes, file_struct):
    size = file_sizes[key]
    for dir in file_struct[key]:
      size += get_file_size(dir, file_sizes, file_struct)
    return size

  soln1()


if __name__ == '__main__':
  main()
