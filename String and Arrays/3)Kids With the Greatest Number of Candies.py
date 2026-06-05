class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_num = max(candies)

        return [True if candies[i]+extraCandies >= max_num else False for i in range(len(candies))]
        