import sys
from helper import get_draw, get_board, parse_inpt

if len(sys.argv) != 3:
  sys.exit("Invalid Command line")


boards = get_board(sys.argv[1])  #getting board input
draws = get_draw(sys.argv[2])   #getting draws input as list

boards_parse = parse_inpt(boards)            #parsing board input as list
boards_reference = parse_inpt(boards)        #making a copy of board_parse for reference to calculate score

winner_board_id = None
last_draw = None

for draw in draws:
  """solving bingo boards"""
  for board in range(0, len(boards_parse)):
    for row in range (0, len(boards_parse[board])):
      for x in range(0, len(boards_parse[board][row])):
        if boards_parse[board][row][x] == draw:
          boards_parse[board][row][x] = "S"

  """checking for winnner board"""
  for board in boards_parse:
    """checking rows"""
    for row in board:
      if row == ["S" for _ in range(0, len(row))]:
        winner_board_id = board
        print(board, "is the winner")
        break
    
    """checking columns"""
    for col in range(0, len(board[0])):
      tmp = []
      for row in range(0, len(board)):
        tmp.append(board[row][col])
      if tmp == ["S" for _ in range(0, len(board))]:
        winner_board_id = board
        break
    
  
  """Break case"""
  if winner_board_id != None:
    last_draw = draw
    break

"""printing winner boards"""
for i in range(0, 5):
  print(winner_board_id[i])

#solving score for winner_board
score = 0
for i in range(0, len(winner_board_id)):
  for j in range(0, len(winner_board_id[i])):
    if winner_board_id[i][j] != "S":
      score += int(winner_board_id[i][j], 10)
score *= int(last_draw)

"""Printing result"""
print("Last draw: ", last_draw)
print("Winner: ", boards_parse.index(winner_board_id))
print("Score: ", score)