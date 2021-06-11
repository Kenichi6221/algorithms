import heapq

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
        dic = {}
        max_continous = 1
        for index, element in enumerate(s):
            if index>0 and s[index]==s[index-1]:
              max_continous +=1
              if element in dic: max_continous = max(max_continous,dic[element])
              dic[element]= max_continous
            else:
              max_continous = 1

        total_repeated_characters = len(dic)
        if total_repeated_characters == 0: return 1
        if total_repeated_characters == 1: return dic[list(dic)[0]]

        max_heap = []
        for value in dic.values():
            heapq.heappush(max_heap,(-value))

        dic=None
        return -heapq.heappop(max_heap)

if __name__ == '__main__':
    s = Solution()
    for word in sys.stdin:
      print(s.maxPower(word))
