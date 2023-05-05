import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Returns the top k frequent elements in nums.

        :param nums: A list of integers.
        :param k: An integer indicating the number of most frequent elements to return.
        :return: A list of k most frequent elements in nums.
        '''
        freq_count = Counter(nums)

        # Use heapq to get the k largest elements by frequency
        # Use nlargest to return the k elements with the highest count
        # The key argument specifies a function to extract a comparison key from each element in the list
        # Use the second element of each tuple (which is the count) as the key
        # Return the first element of each tuple (which is the element itself)
        return [num for num, _ in heapq.nlargest(k, freq_count.items(), key=lambda x: x[1])]
