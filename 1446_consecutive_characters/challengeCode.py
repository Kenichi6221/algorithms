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
    def maxPower(self, s: str) -> int:
        max_continous = globalMax = 1
        start,explorer = 0,1
        size = len(s)
        while explorer<size:
            if s[start] == s[explorer]:
                max_continous += 1
                globalMax = max(globalMax,max_continous)
            else:
                max_continous = 1
            start+=1
            explorer+=1
        return globalMax

if __name__ == '__main__':
    s = Solution()
    for word in sys.stdin:
      print(s.maxPower(word))
