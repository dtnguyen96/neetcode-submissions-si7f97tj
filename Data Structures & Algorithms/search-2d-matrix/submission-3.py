"""
1. Find the row that stores the target using binary search
2. If the top <= bot is not true, which means we have 
already crossed out all the rows, and no rows contain the target value.
 So we should return False. 
3. Find the target in the row using binary search 

Pseudocode
1. Find the length of row and cols 
2. Top row will be 0, bot row will be len(row) - 1
3. While top <= bot: 
    a. Find mid 
    b. if target > 
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1 
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break 
        
        if not (top <= bot):
            return False 
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False 