class Solution:
    # Function to rotate matrix 90 degrees clockwise in-place
    def rotateClockwise(self, matrix):
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                # Swap element at (i, j) with (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            # Reverse the current row to simulate clockwise rotation
            matrix[i].reverse()

# Driver code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

obj = Solution()
obj.rotateClockwise(matrix)

# Print rotated matrix
for row in matrix:
    print(*row)
