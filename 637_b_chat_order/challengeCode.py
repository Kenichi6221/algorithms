import sys
from typing import List

class Solution:
  def print_chat_order(self,chat_stack:List[str]):
    already_printed_dictionary = {}
    while chat_stack:
      name = chat_stack.pop()
      if name not in already_printed_dictionary:
        already_printed_dictionary[name] = 1
        print(name)

if __name__ == '__main__':
  total_messages = int(sys.stdin.readline().rstrip())
  stack:List[str] = []
  s = Solution()
  for _ in range(total_messages):
    name = sys.stdin.readline().rstrip()
    stack.append(name)
  s.print_chat_order(stack)
