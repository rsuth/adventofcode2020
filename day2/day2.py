import re

good_part1 = 0
good_part2 = 0

with open('input.txt', 'r') as infile:
  for line in infile:
    m = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
    lower = int(m.group(1))
    upper = int(m.group(2))
    char = m.group(3)
    password = m.group(4)
    
    if lower <= password.count(char) <= upper:
      good_part1 += 1
    
    if (password[lower-1] == char) ^ (password[upper-1] == char):
      good_part2 += 1

print(good_part1)
print(good_part2)