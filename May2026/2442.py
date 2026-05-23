class Solution:
    def reverse(self, a: int) -> int:
        rev = 0
        while a > 0:
            rev = (rev*10) + (a%10)
            a//= 10
        return rev

    def countDistinctIntegers(self, nums: list[int]) -> int:
        ans = set()
        for num in nums:
            ans.add(num)
            ans.add(self.reverse(num))
        return len(ans)