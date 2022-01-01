import sys

#get input
raw_input = None
with open(sys.argv[1], "r") as input_f:
	raw_input = input_f.read()

#parsing input data
inputs = raw_input.split("\n")
for i in range(len(inputs)):
	inputs[i] = inputs[i].split(" -> ")

#find largest x and y coordinate
x = y = 0
for input in inputs:
	for inp in input:
		tmp_l = inp.split(",")
		#checking x-coordinate
		if int(tmp_l[0]) > x:
			x = int(tmp_l[0])
		#checking y-coordinate
		if int(tmp_l[1]) > y:
			y = int(tmp_l[1])

#creating 2d list to map vents
vents_map = []
for y_cor in range(y + 1):
	vents_map.append([0 for _ in range(x + 1)])


"""
plotting points on the vents_map from the input_data
and increment the value of the coordinate by 1
"""
for input in inputs:
	coor1, coor2 = input[0].split(","), input[1].split(",")
	x1, y1, x2, y2 = int(coor1[0]), int(coor1[1]), int(coor2[0]), int(coor2[1])
	if x1 == x2:												#considering only vertical line
		start_y = y1 if y1 < y2 else y2
		end_y = y1 if y1 >= y2 else y2
		"""plotting coordinate on vents_map"""
		for vent in range(start_y, end_y + 1):
			vents_map[vent][x1] += 1

	elif y1 == y2:											#considering only horizontal line
		start_x = x1 if x1 < x2 else x2
		end_x = x1 if x1 >= x2 else x2
		"""plotting coordinate on vents_map"""
		for vent in range(start_x , end_x + 1):
			vents_map[y1][vent] += 1

			
	"""to determine the number of points where at least two lines overlap. This is anywhere
	in the vent_map with a 2 vent or larger """
	result = 0
	for row in vents_map:
		for vent in row:
			if vent >= 2:
				result += 1


#printing vent_map 
for row in vents_map:
	print(f"{row} \n")
print("RESULT: ", result)