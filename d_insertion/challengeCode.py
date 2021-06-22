import sys
if __name__ == '__main__':

  size = int(sys.stdin.readline())-1
  line = sys.stdin.readline().rstrip()

  balance = 0
  missing_open = 0
  missing_close = 0

  # totalize missing open brackets
  for element in line:
    if element == '(':
      balance+= 1
    else:
      balance-= 1
    if balance<0:
      missing_open = min(missing_open,balance)

  # totalize missing open brackets
  balance = 0
  while size>=0:
    if line[size] == ")":
      balance+=1
    else:
      balance-=1
    if balance<0:
      missing_close = min(missing_close,balance)
    size-=1
  print("("*(-missing_open)+ line +")"*(-missing_close))