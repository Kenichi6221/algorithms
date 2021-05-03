from sys import stdin
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      unsorted_pointer = 0
      size = len(nums)-1
      numberVisited = 2**(size)-1
      while unsorted_pointer<=size:
        alreadyVisited = numberVisited & (1 << (nums[unsorted_pointer]-1))
        if alreadyVisited == 0:
          return nums[unsorted_pointer]
        numberVisited = numberVisited & ~(1 << (nums[unsorted_pointer]-1))
        unsorted_pointer = nums[unsorted_pointer]

if __name__ == '__main__':
  solution = Solution()
  for line in stdin:
    nums = [int(element) for element in line.split(",")]
    solution.findDuplicate(nums)
    print(solution.findDuplicate(nums))