class Fenwick:
    def __init__(self, m):
        self.arr = [0] * (m * 2 + 1)
        for i in range(m):
            idx = i + 1 + m
            self.arr[idx] += 1
            immediate_parent = idx + (idx & -idx)
            if immediate_parent < len(self.arr):
                self.arr[immediate_parent] += self.arr[idx]
    
    def add(self, i, a):
        while i < len(self.arr):
            self.arr[i] += a
            i += i & -i
    
    def sum(self, i):
        total = 0
        while i > 0:
            total += self.arr[i]
            i -= i & -i
        return total

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        vimap = {}
        fenwick = Fenwick(m)
        ans = []
        for i in range(1, m + 1):
            vimap[i] = i + m
        curr = m
        for i, query in enumerate(queries):
            idx = vimap[query]
            ans.append(fenwick.sum(idx) - 1)
            fenwick.add(idx, -1)
            vimap[query] = curr
            fenwick.add(curr, 1)
            curr -= 1
        return ans