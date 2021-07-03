class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_match = 0
        while n>1:
            if n & 1:
                total_match += (n-1)//2
                n = (n - 1) // 2 + 1
            else:
                total_match += n//2
                n = n//2
        return total_match