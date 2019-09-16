class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        base_row = 0
        base_col = 0

        curr_row = 0
        curr_col = 0

        num_rotated = 0

        prev = matrix[0][0]

        while num_rotated < len(matrix) ** 2:
            new_row = curr_col
            new_col = len(matrix) - curr_row - 1

            temp = matrix[new_row][new_col]
            matrix[new_row][new_col] = prev
            prev = temp
            num_rotated += 1

            if num_rotated == len(matrix) ** 2:
                break

            if new_row == base_row and new_col == base_col:
                if base_col < len(matrix) - 2 - base_row:
                    base_col += 1
                else:
                    base_row += 1
                    base_col = base_row

                curr_row, curr_col = base_row, base_col
                prev = matrix[base_row][base_col]
            else:
                curr_row = new_row
                curr_col = new_col
