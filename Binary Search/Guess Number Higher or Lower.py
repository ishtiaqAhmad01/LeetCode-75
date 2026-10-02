# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while True:
            num = (left + right) // 2

            a = guess(num)
            if a == 1:
                left = num + 1
            elif a == -1:
                right = num - 1
            else:
                return num

            
