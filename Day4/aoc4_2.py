import sys
from helper import get_draw, get_board, parse_inpt


if len(sys.argv) != 3:
  sys.exit("Invalid Command line")


boards = get_board(sys.argv[1])  #getting board input
draws = get_draw(sys.argv[2])   #getting draws input as list

boards_parse = parse_inpt(boards)            #parsing board input as list
boards_reference = parse_inpt(boards)        #making a copy of board_parse for reference to calculate score

winner_board_id = []
last_draw = None
total_board = len(boards_parse)

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
        if boards_parse.index(board) not in winner_board_id:
          winner_board_id.append(boards_parse.index(board))
        break
    
    """checking columns"""
    for col in range(0, len(board[0])):
      tmp = []
      for row in range(0, len(board)):
        tmp.append(board[row][col])
      if tmp == ["S" for _ in range(0, len(board))]:
        if boards_parse.index(board) not in winner_board_id:
          winner_board_id.append(boards_parse.index(board))
        break
    
  
  """Break case"""
  if len(winner_board_id) == total_board:
    print(total_board)
    last_draw = draw
    break

print("Winner board-ID according to their winning order: ", winner_board_id)

"""printing winner boards"""
for i in range(0, 5):
  print(boards_parse[winner_board_id[-1]][i])
print()
for i in range(0, 5):           #printing for reference
  print(boards_reference[27][i])

#solving score for winner_board
last_win = boards_parse[winner_board_id[-1]]
score = 0
for i in range(0, len(last_win)):
  for j in range(0, len(last_win[i])):
    if last_win[i][j] != "S":
      score += int(last_win[i][j])
score *= int(last_draw)

"""Printing result"""
print("Last draw: ", last_draw)
print("Last Winner ID: ", winner_board_id[-1])
print("Score: ", score)


"""
The last board winner is a special case because when the last draw is selected on that board, the boards get a complete selected row and a column. This is not a mistake, 
of the algorithm which I thought at first but a special case due to the special arrangement of the numbers on the board
So, this is what happen:
The board has one incomplete filled row with only one number left and also one incomplete filled column with only one number left
But this unselected number on the board lies in the intersection of the mentioned incomplete row and column
So, when this number is selected, we get a complete selected row and a column
Peace, HAPPY CODING ヽ(´▽`)/
"""