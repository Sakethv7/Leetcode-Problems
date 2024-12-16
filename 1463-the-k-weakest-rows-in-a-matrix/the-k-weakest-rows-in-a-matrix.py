class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 1s (soldiers) are at left of 0s (civilians)
        # row i is weaker than row j if : - no. of soldiers in row i < no. of soldiers in row j or both rows have the same number of soldiers and i<j 

        # return the indices of k weakest rows in the matrix ordered from weakest to strongest
#         count_soldiers = []

#         for i in range(len(mat)):  # Calculate the number of soldiers for each row
#             soldiers = sum(mat[i]) #count the number of soldiers(1s) in the row 
#             count_soldiers.append((soldiers, i))
        
#         count_soldiers.sort()

#         return [index for _, index in count_soldiers[:k]]
                
#  #O(m*n + mlog)
        def count_soldiers(row):
            low, high = 0, len(row)  # Binary search boundaries
            while low < high:
                mid = (low + high) // 2
                if row[mid] == 1:  # If 1, move to the right half
                    low = mid + 1
                else:  # If 0, move to the left half
                    high = mid
            return low  # Position of the first 0 == count of soldiers
        
        count_soldiers_list = [(count_soldiers(row), i) for i, row in enumerate(mat)]

        count_soldiers_list.sort()

        return [i for _, i in count_soldiers_list[:k]]
        


