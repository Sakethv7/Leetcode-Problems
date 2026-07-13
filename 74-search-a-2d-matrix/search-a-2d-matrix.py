class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row*col-1

        while left <= right:
            mid = (left+right)//2
            idx_row = mid // col
            idx_col = mid%col

            if matrix[idx_row][idx_col] == target:
                return True
            elif matrix[idx_row][idx_col] > target:
                right = mid - 1
            else:
                left = mid+1
            
        return False 