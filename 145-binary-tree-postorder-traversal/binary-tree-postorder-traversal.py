# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        curRoot = [root.val]
        rightTree = self.postorderTraversal(root.right)
        leftTree = self.postorderTraversal(root.left)
        return leftTree + rightTree + curRoot