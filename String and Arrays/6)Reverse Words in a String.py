class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")

        s = [word for word in s if word!=""]        
        s.reverse()
        return " ".join(s)
        