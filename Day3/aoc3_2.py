from os import cpu_count
import sys

def get_input(file_name):
  input_data = []
  with open(file_name, "r") as src:
    for line in src:
      input_data.append(line.strip()) 
  return input_data

if (len(sys.argv)) != 2:
  sys.exit("Input file missing")
  
inputs_oxy = inputs_co = get_input(sys.argv[1])
tmp_rating = []
oxy_selector = ""
co_selector = ""

#Oxygen generator rating
for i in range(0, len(inputs_oxy[0])):
  zero_count = one_count = 0
  #break loop if only one element is remained in inputs element
  if len(inputs_oxy) == 1:
    break
  #Selector condition for oxygen generator
  for input in inputs_oxy:
    if input[i] == "0":
      zero_count += 1
    else:
      one_count += 1
  if zero_count > one_count:
    oxy_selector = "0"
  else:
    oxy_selector = "1"

  #removing element from list based on selector
  for input in inputs_oxy:
    if input[i] == oxy_selector:
      tmp_rating.append(input)
  inputs_oxy = tmp_rating
  tmp_rating = []

#Carbon dioxide scrubber rating
for i in range(0, len(inputs_co)):
  zero_count = one_count = 0
  #loopp break condition
  if len(inputs_co) == 1:
    break
  #selector condition for CO Scrubber
  for input in inputs_co:
    if input[i] == "0":
      zero_count += 1
    else:
      one_count += 1
  if zero_count > one_count:
    co_selector = "1"
  else:
    co_selector = "0"
  for input in inputs_co:
    if input[i] == co_selector:
      tmp_rating.append(input)
  inputs_co = tmp_rating
  tmp_rating = []


oxy_rating = int(inputs_oxy[0], base=2)
co_rating = int(inputs_co[0], base=2)

print("Oxy: ", oxy_rating)
print("CO: ", co_rating)

print(f"Result: {oxy_rating * co_rating}")
