#helper function

input_data = []

def get_input(file_name):
  with open(file_name, "r") as src:
    for line in src:
      input_data.append(line.strip())
    
  return input_data