import sys

def get_input(file_name):
  input_data = []
  with open(file_name, "r") as src:
    for line in src:
      input_data.append(line.strip()) 
  return input_data

if (len(sys.argv)) != 2:
  sys.exit("Input file missing")
  
inputs = get_input(sys.argv[1])


gamma = epsilon = ""

for i in range(0, len(inputs[0])):
  zero_count = one_count = 0
  for input in inputs:
    if input[i] == "0":
      zero_count += 1
    else:
      one_count += 1
  if zero_count > one_count:
    gamma += "0"
    epsilon += "1"
  else:
    gamma += "1"
    epsilon += "0"

#converting binary to decimal format
gamma_base10 = int(gamma, base = 2)
epsilon_base10 = int(epsilon, base = 2)
print(gamma, epsilon)
print("Result: ", gamma_base10 * epsilon_base10)
