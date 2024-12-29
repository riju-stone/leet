"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    matrix_len = len(matrix) - 1

    # binary search to find target row
    row_low = 0
    row_high = matrix_len
    target_row = -1

    while row_low <= row_high:
        row_mid = (row_low + row_high) // 2

        if target >= matrix[row_mid][0] and target <= matrix[row_mid][-1]:
            target_row = row_mid
            break
        elif target < matrix[row_mid][0]:
            row_high = row_mid - 1
        else:
            row_low = row_mid + 1

    if target_row == -1:
        return False

    # binary search to find target column
    col_low = 0
    col_high = len(matrix[target_row]) - 1

    while col_low <= col_high:
        col_mid = (col_low + col_high) // 2

        if target == matrix[target_row][col_mid]:
            return True
        elif target < matrix[target_row][col_mid]:
            col_high = col_mid - 1
        else:
            col_low = col_mid + 1

    return False


if __name__ == "__main__":
    res = search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 12)
    print(res)
