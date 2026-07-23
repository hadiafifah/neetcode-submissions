class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Each Row
        seen = set()
        for i in range(9):
            seen.clear()
            for j in range(9):
                val = board[i][j]
                if (val != '.') and (val not in seen):
                    seen.add(val) # val is number and not seen before
                elif (val in seen):
                    return False

        # Check Each Column
        for i in range(9):
            seen.clear()
            for j in range(9):
                val = board[j][i]
                if (val != '.') and (val not in seen):
                    seen.add(val) # val is number and not seen before
                elif (val in seen):
                    return False

        # Check Each 3x3 Box
        for boxrow in (0, 3, 6):
            for boxcol in (0, 3, 6):
                seen.clear()
                for i in range(boxrow, boxrow+3):
                    for j in range(boxcol, boxcol+3):
                        val = board[i][j]
                        if (val != '.') and (val not in seen):
                            seen.add(val) # val is number and not seen before
                        elif (val in seen):
                            return False
        
        return True
                

        