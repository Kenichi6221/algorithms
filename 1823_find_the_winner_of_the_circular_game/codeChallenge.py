class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [element for element in range(1,n+1)]
        droped = 0
        p = c =  0
        while droped<n-1:
            p+= 1 if friends[c]>0 else 0
            if p%k==0and p !=0:
                droped+=1
                friends[c] = 0
                c = min(c,len(friends)-1)
                p = 1 if friends[c]>0 else 0
            c = (c+1)%(len(friends))

        return sum(friends)