import re
with open('input.txt', 'r') as infile:
  batch = infile.readlines()

def read_batch(batch):
  current_passport = {}
  passports = []
  batch.append('\n')
  for l in batch:
    if l != '\n':
      current_passport.update({k:v for k,v in [tuple(i.split(':')) for i in l.strip().split(' ')]})
    else:
      passports.append(current_passport)
      current_passport = {}
  return passports

def valid_passports_p1(passports):
  required_fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
  valid_passports = []
  for passport in read_batch(batch):
    if passport.keys() >= required_fields:
      valid_passports.append(passport)
  return valid_passports

def valid_height(hgt):
  m = re.match(r'(\d+)(cm|in)', hgt)
  if m is None:
    return False
  else:
    if m.group(2) == 'in':
      if not (59 <= int(m.group(1)) <= 76):
        return False
    if m.group(2) == 'cm':
      if not (150 <= int(m.group(1)) <= 193):
        return False
  return True

def validate_passport_p2(passport):
  if not (1920 <= int(passport['byr']) <= 2002):
    return False
  if not (2010 <= int(passport['iyr']) <= 2020):
    return False
  if not (2020 <= int(passport['eyr']) <= 2030):
    return False
  if not valid_height(passport['hgt']):
    return False
  if re.match(r'#[a-f\d]{6}$', passport['hcl']) is None:
    return False
  if passport['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
    return False
  if re.match(r'\d{9}$', passport['pid']) is None:
    return False
  return True

present_passports = valid_passports_p1(read_batch(batch))
print(f'part1 - valid count: {len(present_passports)}')

valid_p2 = 0
for p in present_passports:
  if validate_passport_p2(p):
    valid_p2 += 1

print(f'part2 - valid count: {valid_p2}')