from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hash_map = Counter(nums)
        hash_map = sorted(hash_map.items(), key = lambda x:x[1], reverse = True)
        for i in range(k):
            res.append(hash_map[i][0])
        return res