def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        max_length = find_gcd(len(str1), len(str2))
        candidate = str1[:max_length]

        # Check if the candidate perfectly reconstructs BOTH strings
        if (candidate * (len(str1) // max_length) == str1 and 
            candidate * (len(str2) // max_length) == str2):
            return candidate
            
        return ""