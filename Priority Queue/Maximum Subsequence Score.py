class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pairs = [ (n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda n : n[1], reverse=True)

        heap = []
        Sumn1 = 0
        ans = 0

        for n1, n2 in pairs:
            Sumn1 += n1

            heapq.heappush(heap, n1)

            if len(heap) > k:
                Sumn1 -= heapq.heappop(heap)
            if len(heap) == k:
                ans = max(ans, Sumn1 * n2)
        
        return ans
        

             
        





        
