import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<= 0:
            return False
        exponent = math.floor(math.log2(n))
        return 2**exponent == n