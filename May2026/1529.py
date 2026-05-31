class Solution:
    def minFlips(self, target: str) -> int:
        ans = flip = 0
        for bulb in target: 
            if flip ^ int(bulb): 
                flip ^= 1
                ans += 1
        return ans