class Solution:
    partial = {0:0,1:1,2:1}
    def tribonacci(self, n: int) -> int:
        if n in self.partial:
            return self.partial[n]
        self.partial[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.partial[n]