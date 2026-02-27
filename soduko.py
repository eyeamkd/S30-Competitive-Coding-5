'''
Time Complexity: O(9^(n*n)) where n is the size of the board (9 for standard Sudoku)
Space Complexity: 
O(n*n) for the recursion stack
O(n*n) for the board state 
'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])
        rows, cols, boxes = [], [], []
        for i in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())
        def get_board_index(r, c):
            if r<3 and c<3:
                return 0
            if r<3 and c<6:
                return 1 
            if r<3 and c<9:
                return 2 
            if r<6 and c<3:
                return 3
            if r<6 and c<6:
                return 4
            if r<6 and c<9:
                return 5
            if r<9 and c<3:
                return 6
            if r<9 and c<6:
                return 7 
            if r<9 and c<9:
                return 8 
            
        def  calculate_empty_cells(board):
            empty_cells = []
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c]==".":
                        empty_cells.append((r,c))
                    else:
                        rows[r].add(int(board[r][c]))
                        cols[c].add(int(board[r][c]))
                        box_index = get_board_index(r,c)
                        boxes[box_index].add(int(board[r][c]))
                  
            return empty_cells 
        
        empties = calculate_empty_cells(board)

        def solve(index):
            if index==len(empties):
                return True  
            options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            available = []
            r, c = empties[index]
            board_index = get_board_index(r,c)
            for option in options: 
                if option not in rows[r] and option not in cols[c] and option not in boxes[board_index]:
                    available.append(option)
            
            if len(available)==0:
                return False
            
            for available_option in available:
                board[r][c] = str(available_option)
                rows[r].add(available_option)
                cols[c].add(available_option)
                boxes[board_index].add(available_option)
                result = solve(index+1)
                if result:
                    return True 
                else:
                    board[r][c]="."
                    rows[r].remove(available_option)
                    cols[c].remove(available_option)
                    boxes[board_index].remove(available_option) 
            
        solve(0)
        return board

            


            
