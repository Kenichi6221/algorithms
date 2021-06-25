import heapq
from typing import List
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        heap_enqueueTime = []
        heap_processingTimei = []
        index = 0
        for element in tasks:
            enqueueTimei = element[0]
            heapq.heappush(heap_enqueueTime,(enqueueTimei,index))
            index+=1

        total_time = heap_enqueueTime[0][0]
        answer = []
        while heap_enqueueTime:
            while heap_enqueueTime and heap_enqueueTime[0][0]<=total_time:
                enqueueTimei, index = heapq.heappop(heap_enqueueTime)
                heapq.heappush(heap_processingTimei,(tasks[index][1],index))

            if heap_enqueueTime and not heap_processingTimei and heap_enqueueTime[0][0]>total_time:
               total_time+= heap_enqueueTime[0][0]-total_time

            if heap_processingTimei:
                processingTimei,index = heapq.heappop(heap_processingTimei)
                total_time += processingTimei
                answer.append(index)

        while heap_processingTimei:
            _,index =  heapq.heappop(heap_processingTimei)
            answer.append(index)
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.getOrder([[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]))
