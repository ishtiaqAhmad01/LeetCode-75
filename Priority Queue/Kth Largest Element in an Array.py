class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = nums[:k]
        heapq.heapify(heap)

        i = k

        while i < len(nums):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
            i+=1
        
        return heap[0]
