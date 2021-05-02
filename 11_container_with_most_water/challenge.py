from sys import stdin
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
      max_height = max(height)
      min_height = min(height)

      if(max_height == min_height):
        return max_height*(len(height)-1)

      start_pointer = 0
      end_pointer = len(height)-1
      max_capacity = 0

      while(start_pointer<end_pointer):
        base = end_pointer-start_pointer
        start_height = height[start_pointer]
        end_height = height[end_pointer]
        current_capacity = min(start_height,end_height)*base
        max_capacity = max(current_capacity, max_capacity)
        if(start_height<=end_height): start_pointer+=1
        if(start_height>end_height):end_pointer-=1

      return max_capacity

if __name__ == '__main__':
  solution = Solution()
  for line in stdin:
    height = [int(element) for element in line.split(",")]
    print(solution.maxArea(height))