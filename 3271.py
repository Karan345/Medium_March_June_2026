class Solution:
    def stringHash(self, s: str, k: int) -> str:
        check=97
        result, t = "", 0
        sum = 0
        for i intange(len(s)):
            sum += ord(s[i]) - check
            t += 1
            if t == k:
                sum = sum%26
                result += chr(sum+check)
                sum,t = 0,0
        return result