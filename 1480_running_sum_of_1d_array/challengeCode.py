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
    def runningSum(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for index in range(1,size):
            nums[index] = nums[index]+nums[index-1]
        return nums

if __name__ == '__main__':
    s = Solution()
    for line in sys.stdin:
      array = [int(element) for element in line.split(",")]
      print(s.runningSum(array))