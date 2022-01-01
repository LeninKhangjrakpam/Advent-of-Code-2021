import sys
from helper import get_input

if (len(sys.argv)) != 2:
  sys.exit("Input file missing")

#getting data from input file
inputs = get_input(sys.argv[1])

#initialising coordinate
forward = depth = 0

for input in inputs:
  input_parse = input.split()    #splitting string into list
  if input_parse[0] == "forward":
    forward += int(input_parse[1])
  elif input_parse[0] == "up":
    depth -= int(input_parse[1])
  else:
    depth += int(input_parse[1])
  
print("Coordinate: ", forward, depth)
print("RESULT: ", forward * depth)
