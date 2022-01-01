import sys

if len(sys.argv) != 2:
  sys.exit("Missing filename")

#list to store the input
input = []

#getting input from the file
counter = 0
with open(sys.argv[1], "r") as src:
  for line in src:
    input.append(int(line))

#input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]       test case
increased_no = 0

for i in range(1, len(input)):
  if input[i] > input[i - 1]:
    increased_no += 1

print(f"No of Increased: {increased_no}")