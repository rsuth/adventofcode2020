with open('input.txt', 'r') as infile:
  forest = infile.read().splitlines()


def count_trees(forest, slope):
  trees = 0
  pos = (0,0)
  slope = slope

  while pos[0] < len(forest):
    if forest[pos[0]].strip()[pos[1]%len(forest[0])] == '#':
      trees += 1
    pos = tuple(map(sum, zip(pos, slope)))
  return trees

part1 = count_trees(forest, (1,3))
print(part1)

part2_slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]

part2 = 1
for s in part2_slopes:
  part2 *= count_trees(forest, s)

print(part2)
  
  
