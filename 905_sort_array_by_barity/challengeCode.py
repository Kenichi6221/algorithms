from typing import List

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
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start,end=0,len(nums)-1
        while start<end:
            if nums[end]%2==0 and nums[start]&1:
                nums[end],nums[start] = nums[start],nums[end]
            if nums[end]&1:
                end-=1
            if nums[start]%2==0:
                start+=1
        return nums

if __name__ == '__main__':
  s = Solution()
  for line in sys.stdin:
    array = [int(element) for element in line.split(',')]
    print(s.sortArrayByParity(array))
