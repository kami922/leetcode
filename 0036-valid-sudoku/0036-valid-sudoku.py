class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        sub_box_size = 3

        # Check rows
        for row in board:
            seen = set()  # Use a set for efficient checking of unique elements
            for char in row:
                if char == ".":
                    continue  # Skip empty cells
                if char in seen:
                    return False
                seen.add(char)
            # Check columns
        for col in range(cols):
            seen = set()
            for row in range(rows):
                char = board[row][col]
                if char == ".":
                    continue  # Skip empty cells
                if char in seen:
                    return False
                seen.add(char)

        # Check sub-boxes
        for i in range(0, rows, sub_box_size):
            for j in range(0, cols, sub_box_size):
                seen = set()
                for x in range(i, i + sub_box_size):
                    for y in range(j, j + sub_box_size):
                        char = board[x][y]
                        if char == ".":
                            continue  # Skip empty cells
                        if char in seen:
                            return False
                        seen.add(char)

        return True