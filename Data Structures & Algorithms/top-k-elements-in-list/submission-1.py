
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap=[]

        for key in counter.keys():
            heapq.heappush(heap,(- counter[key],key))
            

        result=[]
        for i in range(k):
            result.append(heapq.heappop(heap)[1]) 
        return result




        