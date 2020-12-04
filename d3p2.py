# Advent of Code
# Day 3, Puzzle 2

tree_num1 = 0
tree_num2 = 0
tree_num3 = 0
tree_num4 = 0
tree_num5 = 0

with open('hill_input.txt') as f:
    hill_map = f.read()

hill_map = hill_map.split('\n')

hill_length = len(hill_map) # ==323

#slope 1
for i in range(0, hill_length):
    line = hill_map[i] * hill_length
    spot = line[i]
    if spot == '#':
        tree_num1 += 1
print(tree_num1)

#slope 2
for i in range(0, hill_length):
    line = hill_map[i] * 3 * hill_length
    spot = line[i * 3]
    if spot == '#':
        tree_num2 += 1
print(tree_num2)

#slope 3
for i in range(0, hill_length):
    line = hill_map[i] * 5 * hill_length
    spot = line[i * 5]
    if spot == '#':
        tree_num3 += 1
print(tree_num3)

#slope 4
for i in range(0, hill_length):
    line = hill_map[i] * 7 * hill_length
    spot = line[i * 7]
    if spot == '#':
        tree_num4 += 1
print(tree_num4)

#slope 5
for i in range(0, hill_length, 2):
    line = hill_map[i] * hill_length
    spot = line[i]
    if spot == '#':
        tree_num5 +=1
print(tree_num5)

print(tree_num1 * tree_num2 * tree_num3 * tree_num4 * tree_num5)
