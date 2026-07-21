class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so first we's use a hashmap to register the frequancies of the nums
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # soo turns out there's a better and efficient way to do this 
        # instead of sorting and then slicing - we would be using a heap  
        # sorted_items = sorted(count.items(), key=lambda x:x[1], reverse=True)
        # imp heapq
        sorted_items = heapq.nlargest(k, count.items(), key = lambda x: x[1])
        top_k = sorted_items[:k]
        
        return [x[0] for x in top_k]
