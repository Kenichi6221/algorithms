## only in local windows test
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
    def sumOfUnique(self, nums: List[int]) -> int:
      dictionary = [-1]*101
      total = 0
      for element in nums:
          if dictionary[element] != -1:
              total -= dictionary[element]
              dictionary[element] = 0
          else:
              total += element
              dictionary[element] = element
      return total

if __name__ == '__main__':
    s = Solution()
    for line in sys.stdin:
      array = [int(element) for element in line.split(",")]
      print(s.sumOfUnique(array))