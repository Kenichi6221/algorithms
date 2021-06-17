class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        size = len(s)
        goal_size = len(goal)
        if size!= goal_size: return False
        if s == goal: return True
        result = list(s)
        for _ in range(size):
            result = result[1:]+[result[0]]
            if "".join(result) == goal:return True
        return False