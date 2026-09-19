class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = []
        self.current_num = 1
        self.already_exsist = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.heap) > 0:
            a = heapq.heappop(self.heap)
            self.already_exsist.remove(a)
            return a
        
        self.current_num += 1
        return self.current_num-1

        
    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.current_num > num and num not in self.already_exsist:
            self.already_exsist.add(num)
            heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
