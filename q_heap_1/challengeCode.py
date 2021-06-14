import heapq
import sys

## only to in local windows test
import os
import sys

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
      self._actions = {
          1: lambda x : self.inser_element(x),
          3: lambda x: self.print_min_element(),
          2: lambda x: self.delete_element(x)
        }

  def execute_action(self,action, value=0):
      self._actions[action](value)

  def print_min_element(self):
      if len(self._min_heap)>0:
        print(self._min_heap[0])

  def inser_element(self,element):
      heapq.heappush(self._min_heap,element)

  def pop_minimum(self):
      heapq.heappop(self._min_heap)

  def SearchElement(self, element):
    size = len(self._min_heap)
    explorer,lastChecked = 0,0
    while explorer<size//2 and self._min_heap[explorer]<element:
      if self._min_heap[explorer] == element:
        return explorer

      next = explorer<<1
      if self._min_heap[next+1] == element:
        return next+1
      elif self._min_heap[next+1] < element:
        next = next+1
      else:
        next = next+2
      lastChecked = explorer
      explorer = next

    for index in range(lastChecked,size):
      if self._min_heap[index] == element:
        return index

    return -1

  def replace_val(self, element):
    index = self.SearchElement(element)
    if index == 0:
      heapq.heappop(self._min_heap)
    if index>0:
      self._min_heap[index] = heapq.nlargest(1,self._min_heap)[0]
      self._min_heap.pop()
      heapq.heapify(self._min_heap)

  def delete_element(self, element):
        if len(self._min_heap) == 0:
          return
        self.replace_val(element)


if __name__ == '__main__':
    s = Solution()
    total_queries = int(sys.stdin.readline())
    for _ in range(total_queries):
      instruction = f"{sys.stdin.readline()} 0".replace("/n","")
      [action, value] = [int(element) for element in  instruction.split(" ")[0:2]]
      s.execute_action(action,value)
