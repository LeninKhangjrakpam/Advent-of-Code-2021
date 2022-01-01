#Helper function for AOC_4

def get_draw(fn):
  with open(fn, "r") as f:
    dr = f.read().strip().split(",")
    return dr

def get_board(file):
  with open(file, "r") as src:
    return src.read()

def parse_inpt(boards):
  boards = boards.split("\n\n")
  for i in range(0, len(boards)):
    boards[i] = boards[i].split("\n")
    for j in range(0, len(boards[i])):
      boards[i][j] = boards[i][j].split()
  return boards
