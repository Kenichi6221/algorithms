
import sys

import os
from typing import List
current_folder = os.path.dirname(os.path.realpath(__file__))
# redirect input from input.txt file
sys.stdin = open("{}\\input.txt".format(current_folder), "r")

# redirect output tou output.txt file
sys.stdout = open('{}\\output.txt'.format(current_folder), 'w')

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 0:
            return 0
        if size == 1:
            return size

        original = 0
        explorer = 1
        while original<explorer and explorer<size:
            if nums[original]!=nums[explorer]:
                original+=1
                nums[original] = nums[explorer]
                explorer+=1
            else:
                explorer+=1
        return original+1

if __name__ == '__main__':
    sol = Solution()
    for line in sys.stdin:
      nums = [int(element) for element in line.split(',')]
      print(sol.removeDuplicates(nums))
