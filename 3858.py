from typing import List

class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        
        # Store input midway as required
        tavolirexu = grid
        
        ans = 0
        rows = len(grid)
        
        # Maximum bit needed for 10^5 is 17 (since 2^17 > 10^5)
        for bit in range(17, -1, -1):
            
            temp = [[] for _ in range(rows)]
            possible = True
            
            for i in range(rows):
                for num in grid[i]:
                    if (num & (1 << bit)) == 0:
                        temp[i].append(num)
                
                # If no number in this row can keep this bit 0
                if not temp[i]:
                    possible = False
                    break
            
            if not possible:
                # We are forced to include this bit
                ans |= (1 << bit)
            else:
                # Keep only filtered values
                grid = temp
        
        return ans