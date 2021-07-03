class Solution:
    def numberOfMatches(self, n: int) -> int:
        def find_total_matches(n:int,total_match:int):
            if n == 1:
                return total_match
            if n & 1:
                total_match += (n-1)//2
                n = (n - 1) // 2 + 1
            else:
                total_match += n//2
                n = n//2
            return find_total_matches(n,total_match)
        result = find_total_matches(n,0)
        return result