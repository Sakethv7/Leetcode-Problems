class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]] # Initialize the result with the first row [1]

        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]  # Pad the last row with zeros on both sides to facilitate pairwise addition
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])  # Generate the current row by adding adjacent elements in the padded row
            res.append(row)
        return res