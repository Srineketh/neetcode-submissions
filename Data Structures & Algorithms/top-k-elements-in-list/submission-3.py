class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for i in nums:
            freqMap[i] = freqMap.get(i,0) + 1
        
        heap = []
        for keys,val in freqMap.items():
            heapq.heappush(heap,(val,keys))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res