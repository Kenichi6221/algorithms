from posixpath import split
import sys
from typing import List

if __name__ == '__main__':
    total_users = int(sys.stdin.readline())
    stack_result = [1]
    limit = (2**32)
    res = 0
    overflow = False
    for _ in range(total_users):
      line = sys.stdin.readline().rstrip()
      if "for" in line:
        [_,value] = line.split(" ")
        stack_result.append(min(limit,stack_result[-1]*int(value)))
      elif "end" in line:
        stack_result.pop()
      else:
        overflow = limit-stack_result[-1]<=res
        if not overflow:
          res+=stack_result[-1]
      if overflow:
        print ("OVERFLOW!!!")
        break
    if not overflow:
      print(res)
