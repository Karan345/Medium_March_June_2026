class Solution:
    def simulate(self, start_pos: list[int], n: int, s: str, start: int) -> int:
        moves: int = 0
        row: int = start_pos[0]
        col: int = start_pos[1]
        pointer: int = start
        while pointer < len(s):
            is_valid: bool = True
            match s[pointer]:
                case 'U':
                    if not row: is_valid = False
                    else: row -= 1
                case 'D':
                    if row == n - 1: is_valid = False
                    else: row += 1
                case 'R':
                    if col == n - 1: is_valid = False
                    else: col += 1
                case 'L':
                    if not col: is_valid = False
                    else: col -= 1
            if not is_valid: break
            moves += 1
            pointer += 1
        return moves
    
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m: int = len(s)
        output: list[int] = [0] * m
        for i in range(m):
            output[i] = self.simulate(startPos, n, s, i)
        return output