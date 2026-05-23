class Solution:
    def maxDistinct(self, s: str) -> int:
       #1 liner return len(set(s))
       #Using Dictionary

       dict = {} #Dictionary will save non-repeated characters
       for ch in s:
            if ch not in dict:
                dict[ch] = 1
            else :
                dict[ch] += 1
       return len(dict)