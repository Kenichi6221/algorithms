from sys import stdin
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      start=index = 0
      end = len(nums)-1
      positionDictionary = {}

      if(end==1):
        return [0,1]

      while start<=end:
        if(nums[start] in positionDictionary):
          storednumber = positionDictionary[nums[start]]
          return [start,storednumber]
        positionDictionary[target-nums[start]] = start

        if(nums[end] in positionDictionary):
          storednumber = positionDictionary[nums[end]]
          return [end,storednumber]
        positionDictionary[target-nums[end]] = end
        start+=1
        end-=1

if __name__ == '__main__':
  solution = Solution()
  for line in stdin:
      [array,target] = line.split(" ")
      target = int(target)
      array = [int(element) for element in array.split(",") ]
      print(solution.twoSum(array,target))
