import heapq
import sys
import time
## only to in local windows test
import os
import sys
import math

from typing import List
current_folder = os.path.dirname(os.path.realpath(__file__))
# redirect input from input.txt file
sys.stdin = open("{}\\input.txt".format(current_folder), "r")

# redirect output tou output.txt file
sys.stdout = open('{}\\output.txt'.format(current_folder), 'w')
##

class Solution:
  def __init__(self) -> None:
      self._min_heap = []
      self._deleted = []
      self.count = 0
      self._actions = {
          1: lambda x : self.insert_element(x),
          3: lambda x: self.print_min_element(),
          2: lambda x: self.delete_element(x)
        }

  def execute_action(self,action, value=0):
      self._actions[action](value)

  def insert_element(self,element):
     heapq.heappush(self._min_heap,element)
     self.count+=1

  def print_min_element(self):
      if self.count>0:
        print(self._min_heap[0])

  def delete_element(self, element):
    if self.count<1:
      return
    if self._min_heap[0] == element:
      heapq.heappop(self._min_heap)
      self.count-=1
    else:
      heapq.heappush(self._deleted,element)

    while self._deleted and self._deleted[0]==self._min_heap[0]:
      heapq.heappop(self._min_heap)
      heapq.heappop(self._deleted)
      self.count-=1

if __name__ == '__main__':
    start_time = time.time()
    s = Solution()
    total_queries = int(sys.stdin.readline())
    for _ in range(total_queries):
      instruction = f"{sys.stdin.readline()} 0".replace("/n","")
      [action, value] = [int(element) for element in  instruction.split(" ")[0:2]]
      s.execute_action(action,value)
    print(f"---% seconds --- {time.time()-start_time}")
