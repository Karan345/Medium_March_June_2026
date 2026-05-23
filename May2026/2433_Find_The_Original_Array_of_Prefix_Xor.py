class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans=[]
        prev=0
        for num in pref:
            val=prev^num
            prev=num
            ans.append(val)
        return ans