class Solution:
    partial = {0:0,1:1,2:1}
    last_included = 2
    def tribonacci(self, n: int) -> int:
        if n in self.partial:
            return self.partial[n]
        for nth in range(self.last_included+1,n+1):
            self.partial[nth] = self.partial[nth-1]+self.partial[nth-2]+self.partial[nth-3]
        self.last_included = n
        return self.partial[n]