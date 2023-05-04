class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Returns a matrix of integers in spiral order, starting from the top left corner and
        moving clockwise.

        :param n: An integer representing the dimension of the square matrix to generate.
        :return: A 2D list of integers in spiral order.
        """
        matrix = [[0] * n for _ in range(n)]
        row_start, col_start = 0, 0
        current_index, border_width = 0, 1
        border_center = n // 2

        # Helper function to add the elements of the top border to the matrix
        def add_top_border():
            nonlocal current_index
            for col in range(col_start, n - border_width):
                current_index += 1
                matrix[row_start][col] = current_index

        # Helper function to add the elements of the right border to the matrix
        def add_right_border():
            nonlocal current_index
            for row in range(row_start, n - border_width):
                current_index += 1
                matrix[row][n - border_width] = current_index

        # Helper function to add the elements of the bottom border to the matrix
        def add_bottom_border():
            nonlocal current_index
            for col in range(n - border_width, col_start, -1):
                current_index += 1
                matrix[n - border_width][col] = current_index

        # Helper function to add the elements of the left border to the matrix
        def add_left_border():
            nonlocal current_index
            for row in range(n - border_width, row_start, -1):
                current_index += 1
                matrix[row][col_start] = current_index

        # Iterate over each border of the matrix in clockwise order
        for loop in range(border_center):
            add_top_border()
            add_right_border()
            add_bottom_border()
            add_left_border()
            row_start += 1
            col_start += 1
            border_width += 1

        # If the matrix has an odd dimension, add the center element
        if n % 2 == 1:
            matrix[border_center][border_center] = current_index + 1

        return matrix