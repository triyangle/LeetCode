class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for i in range(len(board)):
            row = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

        # check each col
        for j in range(len(board)):
            col = set()
            for i in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in col:
                        return False
                    col.add(board[i][j])

        # check each sub-box
        for sub_box_num in range(9):
            sub_box = set()
            row_multiplier = sub_box_num // 3
            col_multiplier = sub_box_num % 3

            for i in range(row_multiplier * 3, (row_multiplier + 1) * 3):
                for j in range(col_multiplier * 3, (col_multiplier + 1) * 3):
                    if board[i][j] != ".":
                        if board[i][j] in sub_box:
                            return False
                        sub_box.add(board[i][j])

        return True
