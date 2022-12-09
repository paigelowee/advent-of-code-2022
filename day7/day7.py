def main():
  def soln1():
    with open('day7/input.txt', 'r') as file:
      # maintain current path
      path = ['/']
      file_sizes = {}
      for line in file:
        line = line.replace('\n', '')

        # handle commands (directory navigation)
        if line.startswith('$'):
          print(line)
          if ' cd ' in  line:
            directory = line.strip('$ cd')
            print(directory)
            if directory == '/':
              path = ['/']
            elif directory == '..':
              path.pop()
            else:
              path.append(directory)
        print(path)

        # handle directory content
        # else:
        #   if not line.startswith('dir'):
        #     size = int(line.split(' ')[0])
        #     current_path = ''
        #     # print(path)
        #     for directory in path:
        #       print(directory)
        #       print(current_path)
        #       current_path += directory + '/' if directory != '/' else '/'
        #       file_sizes[current_path] = file_sizes.get('current_path', 0) + size

      print(file_sizes)


      print(path)
  soln1()

if __name__ == '__main__':
  main()