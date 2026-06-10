class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        to_insert = 0
        i = 0

        while i < len(nums):
            if nums[i] != 0:
                nums[to_insert] = nums[i]
                to_insert+=1
            i+=1
        while to_insert < len(nums):
            nums[to_insert] = 0
            to_insert+=1
            
        #print(nums)
