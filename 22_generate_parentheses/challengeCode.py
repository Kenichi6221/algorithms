from typing import List

class Solution:
    def backtrack(self, partial, result ,open_parentesis, close_parentesis, n):
        if open_parentesis ==  n and close_parentesis == n:
            result.append("".join(partial))
        if open_parentesis<n:
            partial.append("(")
            self.backtrack(partial, result ,open_parentesis+1, close_parentesis,n)
            partial.pop()
        if close_parentesis<open_parentesis:
            partial.append(")")
            self.backtrack(partial, result ,open_parentesis, close_parentesis+1,n)
            partial.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack([],result,0,0,n)
        return result
