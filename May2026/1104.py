class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        import math
        level=1
        st=0
        lis=[label]
        for i in range(30):
            if label>st and label<=st+2**i:
                break
            else:
                st+=2**i
            level+=1
        while level >1:
            if level%2==0:
                val=2**level
                val-=label
                val=math.ceil(val/2)
                chk=2**(level-2)
                chk+=val-1
                lis.append(chk)
                label=chk
            else:
                val=2**(level-1)
                val=label-val+1
                val=math.ceil(val/2)
                chk=2**(level-1)
                chk-=val
                lis.append(chk)
                label=chk
            level-=1
        return lis[::-1]