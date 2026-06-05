class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smaller = float("inf")
        middle = float("inf")

        for num in nums:
            print(num, smaller, middle)
            if num <= smaller:
                smaller = num
            elif num <= middle:
                middle = num
            else:
                return True

        return False