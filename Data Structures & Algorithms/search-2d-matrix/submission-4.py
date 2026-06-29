class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_up = 0
        row_down = len(matrix) - 1

        while row_up <= row_down:
            row_mid = (row_up + row_down) // 2

            if target < matrix[row_mid][0]:
                row_down = row_mid - 1

            elif target > matrix[row_mid][-1]:
                row_up = row_mid + 1

            else:
                break

        row = matrix[row_mid]

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if row[mid] < target:
                l = mid + 1

            elif row[mid] > target:
                r = mid - 1

            else:
                return True

        return False