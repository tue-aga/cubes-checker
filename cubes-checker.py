#!/usr/bin/python3

from collections import defaultdict


### Preprocessing ###

# read the path and store it as a list of coordinates
path = []
with open('path.txt') as path_file:
	for line in path_file:
		if line.split():
			path.append(tuple(map(int, line.split())))

# generate dictionary with occupied cells
is_occupied = defaultdict(bool)
for point in path:
	is_occupied[point] = True


### Utility methods ###

# checks if the given coordinate is in range (all coordinates between -10 and 10)
def in_range(coord):
	return (-10 <= coord[0] <= 10 and
		-10 <= coord[1] <= 10 and
		-10 <= coord[2] <= 10)

# returns all neighbors of a given coordinate in the cube grid
def neighbors(coord):
	for i in [-1, 1]:
		p = (coord[0] + i, coord[1], coord[2])
		if in_range(p): yield p
		p = (coord[0], coord[1] + i, coord[2])
		if in_range(p): yield p
		p = (coord[0], coord[1], coord[2] + i)
		if in_range(p): yield p


print('Test results:')


### (1) Check if the construction is a path ###

# computes the degree of a vertex on the path
def degree(coord):
	occupied_neighbors = [n for n in neighbors(coord) if is_occupied[n]]
	return len(occupied_neighbors)

# check if the endpoints have degree 1, and all other vertices have degree 2
def check_path():
	for coord in path:
		if coord == path[0] or coord == path[-1]:
			expected_degree = 1
		else:
			expected_degree = 2
		if degree(coord) != expected_degree:
			return False
	return True

# perform the check
if check_path():
	print('(1) construction is a path')
else:
	print('(1) construction is NOT a path')


### (2) Check if the start point of the path is inside ###

is_outside = defaultdict(bool)

# perform BFS of non-filled cells starting from the given coordinate
def floodfill(coord):
	frontier = [coord]
	while frontier:
		coord = frontier.pop()
		if is_occupied[coord] or is_outside[coord]: continue
		is_outside[coord] = True
		for n in neighbors(coord):
			frontier.append(n)

# we start the BFS at (10, 10, 10) which is definitely outside
floodfill((10, 10, 10))

# checks if the start point of the path is not face-adjacent to an outside cell
def check_inside():
	# we check for all neighbors if they are not outside
	return all(not is_outside[n] for n in neighbors(path[0]))

# perform the check
if check_inside():
	print('(2) endpoint is inside')
else:
	print('(2) endpoint is NOT inside')

