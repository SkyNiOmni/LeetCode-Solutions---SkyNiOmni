class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        answer = True

        for row in board:
            only_nums = []
            for i in row:
                if i != ".":
                    only_nums.append(i)
        
            if len(only_nums) != len(set(only_nums)):
                answer = False
                break
        
        for col in range(9):
            column = []
            for row in range(9):
                column.append(board[row][col])

            only_nums = []
            for i in column:
                if i != ".":
                    only_nums.append(i)

            if len(only_nums) != len(set(only_nums)):
                answer = False
                break
        
        for box_row in range(3):
            for box_col in range(3): 
                box = []

                for r in range(box_row  * 3, box_row * 3 + 3):
                    for c in range(box_col * 3, box_col * 3 + 3):
                        box.append(board[r][c])

                only_nums = []
                for i in box:
                    if i != ".":
                        only_nums.append(i)
                        
                if len(only_nums) != len(set(only_nums)):
                    answer = False  

        return(answer)

            
            

