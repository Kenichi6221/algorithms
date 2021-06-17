class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = []
        close_bracket = {
                    ")":"(",
                    "}":"{",
                    "]":"["
                     }
        for element in s:
            if element in close_bracket:
                if len(open_bracket)>0 and open_bracket[-1] == close_bracket[element]:
                    open_bracket.pop()
                else: return False
            else:
                open_bracket.append(element)
        return len(open_bracket)==0