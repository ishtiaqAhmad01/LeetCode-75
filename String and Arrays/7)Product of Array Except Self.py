class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        prefix_product = []
        for num in nums:
            prefix_product.append(prefix)
            prefix *= num
        
        postfix = 1
        postfix_product = []
        for num in nums[-1::-1]:
            postfix_product.append(postfix)
            postfix *= num
        
        postfix_product.reverse()

        result = []
        for i in range(len(nums)):
            result.append(prefix_product[i] * postfix_product[i])
            
        return result

        