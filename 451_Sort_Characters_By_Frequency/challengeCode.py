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

import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        dict = {}
        for element in s:
            if element in dict:
                dict[element]+=1
            else:
                dict[element]=1

        if len(dict) == 1:
            return s

        frecuencies_dict = []
        for key, value in dict.items():
            heapq.heappush(frecuencies_dict,(-value,key*value))

        dict = None

        result = []
        while frecuencies_dict:
            s,c = heapq.heappop(frecuencies_dict)
            result.append(c)

        return "".join(result)

if __name__ == '__main__':
    s = Solution()
    for line in sys.stdin:
        line = line.replace("\n","")
        print(s.frequencySort(line))