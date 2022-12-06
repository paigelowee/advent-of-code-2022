# Day 2 - rock paper scissors
winning_map = {
  'A': 'Y',
  'B': 'Z',
  'C': 'X'
}

score_map = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

draw_map = {
  'A': 'X',
  'B':'Y',
  'C': 'Z'
}

lose_map = {
  'A': 'Z',
  'B':'X',
  'C': 'Y'
}

def soln1():
  total_score = 0
  with open('day2/input.txt', 'r') as file:
    for line in file:
      moves = line.split()
      p1_move = moves[0]
      p2_move = moves[1]

      # if game is draw, increment by 3
      if draw_map[p1_move] == p2_move:
        total_score = total_score + 3 + score_map[p2_move]
      # if game is won, increment total score
      elif winning_map[p1_move] == p2_move:
        total_score = total_score + 6 + score_map[p2_move]
      # lose
      else:
        total_score += score_map[p2_move]

  print(total_score)

def soln2():
  total_score = 0
  with open('day2/input.txt', 'r') as file:
    for line in file:
      moves = line.split()
      p1_move = moves[0]
      outcome = moves[1]

      # draw
      if outcome == 'Y':
        p2_move = draw_map[p1_move]
        total_score = total_score + 3 + score_map[p2_move]
      # win
      elif outcome == 'Z':
        p2_move = winning_map[p1_move]
        total_score = total_score + 6 + score_map[p2_move]
      # lose
      else:
        p2_move = lose_map[p1_move]
        total_score += score_map[p2_move]

    print(total_score)

if __name__ == '__main__':
  soln1()
  soln2()