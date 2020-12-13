import re

with open('input.txt', 'r') as infile:
  rules = infile.readlines()

bag_rules = {}
for rule in rules: 
  s = rule.strip().split(' contain ')
  outer = re.match(r'^\w+ \w+', s[0]).group(0)
  inner = re.findall(r'\d+ \w+ \w+', s[1])
  inners = []
  for i in inner:
    m = re.match(r'^(\d+) (\w+ \w+)', i)
    qty = int(m.group(1))
    desc = m.group(2)
    for x in range(qty):
      inners.append(desc)
  bag_rules.update({outer:inners})

goal_bag = 'shiny gold'

success_bags = []

def check_bag(bag_rules, outer_bag, goal_bag):
  if goal_bag in bag_rules[outer_bag]:
    return True
  else:
    found = False
    for inner in set(bag_rules[outer_bag]):
      found = check_bag(bag_rules, inner, goal_bag)
      if found:
        break
    return found

for k in bag_rules.keys():
  if check_bag(bag_rules, k, goal_bag):
    success_bags.append(k)

print(len(success_bags))

# part 2
def count_inners(inner_bags):
  if len(inner_bags) == 0:
    return 0
  count = 0
  for bag in set(inner_bags):
    n_bags = inner_bags.count(bag)
    count += (count_inners(bag_rules[bag])+1) * n_bags
  return count

print(count_inners(bag_rules['shiny gold']))
