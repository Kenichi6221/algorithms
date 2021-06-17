import sys
class Solution:
  def plugin(self,s:str)->str:
    size = len(s)
    current =1
    stack = [s[0]]
    while current<size:
      if stack and stack[-1] == s[current]:
        stack.pop()
      else:
        stack.append(s[current])
      current+=1
    return "".join(stack)

if __name__ == '__main__':
    s = Solution()
    for text in sys.stdin:
      print(s.plugin(text))
