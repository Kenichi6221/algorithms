import sys

import os
current_folder = os.path.dirname(os.path.realpath(__file__))
# redirect input from input.txt file
sys.stdin = open("{}\\input.txt".format(current_folder), "r")

# redirect output tou output.txt file
sys.stdout = open('{}\\output.txt'.format(current_folder), 'w')

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      maxSubString = {}
      longest = start=end=0
      stringSize = len(s)

      while start<stringSize and end<stringSize:
        if(s[end] in maxSubString):
          start = max(start,maxSubString[s[end]]+1)
        maxSubString[s[end]] = end
        longest = max(longest,end-start+1)
        end+=1
      return longest

if __name__ == '__main__':
    solution = Solution()
    for line in sys.stdin:
      line = line.replace("\n","")
      longestSubstring = solution.lengthOfLongestSubstring(line)
      print(longestSubstring)