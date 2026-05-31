from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def build_shape(text: str) -> list[int]:
            table = {}
            shape = []
            count = 0
            
            for l in text:
                if l not in table:
                    table[l] = count
                    count += 1
                shape.append(table[l])
            
            return shape
        
        pat_form = build_shape(pattern)
        
        answer = []
        for item in words:
            if build_shape(item) == pat_form:
                answer.append(item)
        
        return answer