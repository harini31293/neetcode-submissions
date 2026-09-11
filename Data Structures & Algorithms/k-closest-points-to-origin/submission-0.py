class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            print(dist)
            #minHeap.append([dist, x, y])
            heapq.heappush(minHeap, [dist, x, y])
        print(minHeap)
        #heapq.heapify(minHeap)
        print(minHeap)
        res = []
        while k >0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -=1
        return res

        