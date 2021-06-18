import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        size = len(points)
        for max_element in range(k):
            point = points[max_element]
            radical = point[0]**2+point[1]**2
            heapq.heappush(max_heap,(-radical,point))

        # After first k elements we can apply pop over original array,
        # that will allow that we recicle the points array when we
        # build the final result
        for max_element in range(k,size):
            point = points.pop()
            radical = point[0]**2+point[1]**2
            heapq.heappushpop(max_heap,(-radical,point))

        # recicle points array to return the k closets points
        for max_element in range(k):
            radical, point = heapq.heappop(max_heap)
            points[max_element] = point

        return points