with open('input.txt', 'r') as infile:
  prog = [line.rstrip() for line in infile]

def run(prog):
  pc = 0
  accumulator = 0
  seen = []
  while pc < len(prog):
    if pc in seen:
      return -1, accumulator
    seen.append(pc)
    op = prog[pc].split(' ')[0]
    arg = int(prog[pc].split(' ')[1])
    if op == 'acc':
      accumulator += arg
      pc += 1
    if op == 'jmp':
      pc += arg
    if op == 'nop':
      pc += 1
  return 1, accumulator

print(run(prog)[1])  

def part2(prog):
  for line_no, ins in enumerate(prog):
    op = ins.split(' ')[0]
    arg = ins.split(' ')[1]
    if op in ['jmp', 'nop']:
      if op == 'jmp':
        prog[line_no] = 'nop' + ' ' + arg
      elif op == 'nop':
        prog[line_no] = 'jmp' + ' ' + arg
      result, acc = run(prog)
      if result == 1:
        return acc
      else:
        prog[line_no] = ins

print(part2(prog))