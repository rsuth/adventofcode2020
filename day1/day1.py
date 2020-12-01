seq = []
with open('input.txt', 'r') as infile:
  for l in infile:
    seq.append(int(l))

def find_pair(seq, target_sum):
  for i, n in enumerate(seq):
    for j in seq[i:]:
      if (n + j) == target_sum:
        return n*j
  return None

def find_triplet(seq, target):
  for i, n in enumerate(seq):
    x = target - n
    p = find_pair(seq[i:], x)
    if p:
      return n*p

print(find_pair(seq, 2020))
print(find_triplet(seq, 2020))