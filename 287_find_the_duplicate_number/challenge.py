from sys import stdin
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      unsorted_pointer = 0
      size = len(nums)-1
      visited = {}
      while unsorted_pointer<=size:
        if(nums[unsorted_pointer]==unsorted_pointer+1):
          visited[nums[unsorted_pointer]] = unsorted_pointer
          unsorted_pointer+=1
        else:
          correctPosition = nums[unsorted_pointer]
          if nums[correctPosition] in visited:
            return nums[correctPosition]
          nums[unsorted_pointer],nums[correctPosition]  =nums[correctPosition],nums[unsorted_pointer]
          visited[nums[correctPosition]] = correctPosition

if __name__ == '__main__':
  solution = Solution()
  for line in stdin:
    nums = [int(element) for element in line.split(",")]
    print(solution.findDuplicate(nums))