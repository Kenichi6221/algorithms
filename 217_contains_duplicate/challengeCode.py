import heapq
import math

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

# time complexity: O(n)
# space complexity: O(1) in place
class Solution:
    def containsDuplicate(self, min_heap: List[int]) -> bool:

        if len(min_heap) == 1: return False

        # O(log(n))
        heapq.heapify(min_heap)

        # O(n)
        last_see = -math.inf
        while min_heap:
            min_element = heapq.heappop(min_heap)
            if last_see == min_element:
                return True
            else:
                last_see = min_element
        return False

if __name__ == '__main__':
    s = Solution()
    for line in sys.stdin:
      array = [int(element) for element in line.split(",")]
      print(s.containsDuplicate(array))
