with open('input.txt', 'r') as infile:
  answers = infile.readlines()

def read_groups(answers):
  current_group = set()
  groups = []
  answers.append('\n')
  for l in answers:
    if l != '\n':
      for c in l.strip():
        current_group.add(c)
    else:
      groups.append(len(current_group))
      current_group = set()
  return groups

groups = read_groups(answers)
print(sum(groups))

# part 2
def read_groups_p2(answers):
  current_group = []
  groups = []
  answers.append('\n')
  for l in answers:
    if l != '\n':
      current_group.append(l.strip())
    else:
      if len(current_group) > 0:
        groups.append(current_group)
      current_group = []
  return groups

groups = read_groups_p2(answers)
count = 0
for g in groups:
  # check the first persons answers
  for a in g[0]:
    # count goes up every time an answer 
    # is shared between the whole group
    if all(a in x for x in g):
      count += 1
print(count)
    
