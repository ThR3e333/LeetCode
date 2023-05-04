class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Returns the elements of the input matrix in spiral order, starting from the top left corner and
        moving clockwise.

        :param matrix: A 2D list of integers.
        :return: A list of integers in spiral order.

        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        row_start, col_start = 0, 0
        current_index, border_width = 0, 1
        border_center = min(num_rows, num_cols) // 2
        result = [0] * (num_rows * num_cols)

        # Helper function to add the elements of the top border to the result
        def add_top_border():
            nonlocal current_index
            for col in range(col_start, num_cols - border_width):
                result[current_index] = matrix[row_start][col]
                current_index += 1

        # Helper function to add the elements of the right border to the result
        def add_right_border():
            nonlocal current_index
            for row in range(row_start, num_rows - border_width):
                result[current_index] = matrix[row][num_cols - border_width]
                current_index += 1

        # Helper function to add the elements of the bottom border to the result
        def add_bottom_border():
            nonlocal current_index
            for col in range(num_cols - border_width, col_start, -1):
                result[current_index] = matrix[num_rows - border_width][col]
                current_index += 1

        # Helper function to add the elements of the left border to the result
        def add_left_border():
            nonlocal current_index
            for row in range(num_rows - border_width, row_start, -1):
                result[current_index] = matrix[row][col_start]
                current_index += 1

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
        if min(num_rows, num_cols) % 2 == 1:
            if num_rows > num_cols:
                for row in range(border_center, border_center + num_rows - num_cols + 1):
                    result[current_index] = matrix[row][border_center]
                    current_index += 1
            else:
                for col in range(border_center, border_center + num_cols - num_rows + 1):
                    result[current_index] = matrix[border_center][col]
                    current_index += 1

        return result


