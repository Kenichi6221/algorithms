class Solution(object):
    def findTheWinner(self, n, k):
        friends = [element for element in range(1,n+1)]
        p = 0
        droped = 0
        while droped<n-1:
            p = (p+k-1)%len(friends)
            friends.remove(friends[p])
            droped+=1
        return friends[0]