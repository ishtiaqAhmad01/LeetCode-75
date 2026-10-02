class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        total_cost = 0

        left_heap = costs[:candidates]
        right_heap = []

        left_point = candidates
        right_point = len(costs) - 1

        while right_point >= left_point:
            if len(right_heap) == candidates:
                break
            right_heap.append(costs[right_point])
            right_point -= 1

        heapq.heapify(left_heap)
        heapq.heapify(right_heap)



        while k:
            if len(left_heap) == 0 or len(right_heap) > 0 and right_heap[0] < left_heap[0]:
                total_cost += heapq.heappop(right_heap)
                if right_point >= left_point:
                    heapq.heappush(right_heap, costs[right_point])
                    right_point -= 1
            else:
                total_cost += heapq.heappop(left_heap)
                if left_point <= right_point:
                    heapq.heappush(left_heap, costs[left_point])
                    left_point += 1
            k-=1

        return total_cost



        
