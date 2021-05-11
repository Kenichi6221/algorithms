import math
import sys

import os
current_folder = os.path.dirname(os.path.realpath(__file__))
# redirect input from input.txt file
sys.stdin = open("{}\\input.txt".format(current_folder), "r")

# redirect output tou output.txt file
sys.stdout = open('{}\\output.txt'.format(current_folder), 'w')
class Solution:
    def myPow(self, x: float, y: int) -> float:
        if(y == 1):
            return x

        if(y == 0):
            return 1

        if(y<0):
            return 1/self.myPow(x,-y)

        timesByItself = math.floor(math.log2(y))
        solution = x

        for _ in range(0,timesByItself):
            solution *= solution
        residualPotence = y & ~(1<<timesByItself)
        return solution*self.myPow(x,residualPotence)

if __name__ == '__main__':
    sol = Solution()
    for line in sys.stdin:
        [base, pow] = [float(element) for element in line.split(" ")]
        print(sol.myPow(base,int(pow)))
