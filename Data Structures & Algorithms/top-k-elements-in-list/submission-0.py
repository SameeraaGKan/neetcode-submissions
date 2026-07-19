class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so first we's use a hashmap to register the frequancies of the nums
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        sorted_items = sorted(count.items(), key=lambda x:x[1], reverse=True)
        top_k = sorted_items[:k]
        
        return [x[0] for x in top_k]
