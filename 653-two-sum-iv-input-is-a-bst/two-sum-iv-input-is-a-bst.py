# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sorted_nodes = []
        self.inorder(root,sorted_nodes)
        left = 0
        right = len(sorted_nodes) - 1

        while left < right:
            current_sum = sorted_nodes[left] + sorted_nodes[right]

            if current_sum == k:
                return True  # Found two elements that sum to k
            elif current_sum < k:
                left += 1  # Sum is too small, need a larger number from the left
            else:  # current_sum > k
                right -= 1 # Sum is too large, need a smaller number from the right

        return False # No such pair found


    def inorder(self,root,eleArr):
        if root is None:
            return
        self.inorder(root.left,eleArr)
        eleArr.append(root.val)
        self.inorder(root.right,eleArr)


    