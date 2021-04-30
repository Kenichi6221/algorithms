from sys import stdin

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
    for line in stdin:
      line = line.replace("\n","")
      longestSubstring = solution.lengthOfLongestSubstring(line)
      print(longestSubstring)