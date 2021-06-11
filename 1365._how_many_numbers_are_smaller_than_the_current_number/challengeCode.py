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
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = [0]*101
        for element in nums:
            counter[element]+=1

        for element in range(1,100):
            counter[element]+=counter[element-1]

        result = []
        for element in nums:
          if element >0:
            result.append(counter[element-1])
          else:
            result.append(0)

        return result


if __name__ == '__main__':
    s = Solution()
    for line in sys.stdin:
      array = [int(element) for element in line.split(",")]
      print(*s.smallerNumbersThanCurrent(array))
