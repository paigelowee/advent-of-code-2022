import os, math

def main():
  soln1()

class Monkey:
  def __init__(self, items, operation, test, true, false):
    self.items = items
    self.operation = operation
    self.test = test
    self.true = true
    self.false = false
    self.turns = 0

  def increment_inspection(self):
    self.turns +=1

  def test_outcome(self, x):
    if (x % self.test) == 0:
      return self.true
    else:
        return self.false

  def add_item(self, item):
    self.items.append(item)

  def throw_items(self):
    self.items = []

def initialise_monkey(data):
  items = data[1].replace('Starting items:', '').replace(' ', '').strip().split(',')
  operation = data[2].replace('Operation: new = old ', '').strip()
  test = int(data[3].replace('Test: divisible by ', '').strip())
  true = int(data[4].replace('If true: throw to monkey ', '').strip())
  false = int(data[5].replace('If false: throw to monkey ', '').strip())
  return Monkey(items, operation, test, true, false)

def  get_greatest_denominator(x, y):
  while y != 0:
      (x, y) = (y, x % y)
  return x

def soln1():
  with open(os.path.dirname(__file__) + '/input.txt', 'r') as file:
    data = [line.replace('\n', '') for line in file]

  monkey_array = []
  x = 0
  while x <= len(data):
    monkey_array.append(initialise_monkey(data[x: x+7]))
    x +=7

  # for each round and then monkey, let them have their go
  for round in range(10000):
    for monkey in monkey_array:
      monkey_items = monkey.items
      for item in monkey_items:
        worry = item
        # inspcect
        monkey.increment_inspection()
        op = monkey.operation
        if 'old' in monkey.operation:
          op = monkey.operation.replace('old', worry)

        worry = eval(str(worry)+op)

        # feel relief
        # worry = math.floor(worry/3)
        # # test the outcome
        res = monkey.test_outcome(worry)
        # throw the item to the resultant monkey
        monkey_array[res].add_item(str(worry))

      monkey.throw_items()

  total = []
  for m in monkey_array:
    total.append(m.turns)
  total.sort(reverse=True)
  totals= total[0] * total[1]
  print(totals)

if __name__ == '__main__':
  main()