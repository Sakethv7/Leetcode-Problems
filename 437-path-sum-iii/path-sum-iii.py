# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         def  countPath(node, current_sum, prefix_sum):
#             if not node:
#                 return 0
             
#             current_sum += node.val
#             # Calculate the number of paths that sum to targetSum
#             path_count = prefix_sum.get(current_sum - targetSum, 0)
            
#             # Update the prefix_sums map with the current sum
#             prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

#             # Recurse into left and right subtrees
#             path_count += countPath(node.left, current_sum, prefix_sum)
#             path_count += countPath(node.right, current_sum, prefix_sum)

#             # Backtracking: remove the current sum from the map
#             prefix_sum[current_sum] -= 1

#             return path_count
        
#         return countPath(root, 0, {0: 1})  # Initialize with prefix_sum {0:1}

#brute force:
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        # Helper function to count paths starting from the current node
        def countSumPaths(node, current_sum):
            if not node:
                return 0
            current_sum += node.val

            # Check if the current sum equals the targetSum
            path_count = 1 if current_sum == targetSum else 0

            # Continue searching in the left and right subtrees
            path_count += countSumPaths(node.left, current_sum)
            path_count += countSumPaths(node.right, current_sum)

            return path_count

        # Main function logic:
        # 1. Count paths starting from the current node
        # 2. Count paths in the left subtree
        # 3. Count paths in the right subtree
        return (
            countSumPaths(root, 0) +
            self.pathSum(root.left, targetSum) +
            self.pathSum(root.right, targetSum)
        )
