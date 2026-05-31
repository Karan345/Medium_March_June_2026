import numpy as np

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # 1. Cast the grid directly into a contiguous NumPy array
        G = np.array(grid, dtype=int)
        
        # 2. Compute marginal projections (row and column totals)
        rows = G.sum(axis=1)    # Shape: (m,)
        cols = G.sum(axis=0)    # Shape: (n,)
        
        # 3. Create structural boolean masks for non-isolated lines
        # (rows > 1)[:, None] creates a column mask; (cols > 1)[None, :] creates a row mask
        can_comm_row = rows > 1
        can_comm_col = cols > 1
        
        # Broadcast the masks into an (m x n) matrix of valid communication zones
        valid_zone = can_comm_row[:, None] | can_comm_col[None, :]
        
        # 4. Filter the server matrix against the valid communication zones
        communicating_servers = G & valid_zone
        
        # 5. The total count is simply the sum of the filtered matrix
        return int(communicating_servers.sum())