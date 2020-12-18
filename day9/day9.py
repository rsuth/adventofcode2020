with open('input.txt', 'r') as infile:
  n = []
  for x in infile:
    n.append(int(x.strip()))

for i in range(25, len(n)-1):
  valid = False
  for j in range(26):
    t = n[i]-n[i-j]
    for k in range(26):
      if k == j:
        pass
      elif t == n[i-k]:
        valid = True
        break
  if not valid:
    print(f'found invalid: {n[i]}')
    p1 = n[i]
    break

for x in range(len(n)):
  lg_index = x+2
  while sum(n[x:lg_index]) <= p1:
    if sum(n[x:lg_index]) == p1:
      cont = n[x:lg_index]
      sm = min(cont)
      lg = max(cont)
      print(f'weakness found: {sm+lg}')
      break
    lg_index += 1

    

