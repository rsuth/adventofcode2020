with open('input.txt') as infile:
  passes = infile.readlines()

def split(start, end, p):
  # base case:
  if len(p) == 1:
    if p == 'F' or p == 'L':
      return start
    else:
      return end
  else:
    if p[0] == 'F' or p[0] == 'L':
      return(split(start, start+((end-start)//2), p[1:]))
    else:
      return(split(start+((end-start)//2)+1, end, p[1:]))

def find_seat(p):
  row = split(0, 127, p.strip()[:7])
  col = split(0, 7, p.strip()[-3:])
  return row*8 + col

max_seat = 0
for p in passes:
  seat = find_seat(p)
  if seat > max_seat:
    max_seat = seat

print(max_seat)

# part 2:
seats = [find_seat(p) for p in passes]
seats = sorted(seats)
for i in range(seats[0], seats[-1]+1):
  if i not in seats:
    print(i)
  
