# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self,root,k,seen):
        if root == None:
            return False

        if k-root.val in seen:
            return True
        seen.add(root.val)
        return self.inorderTraversal(root.left,k,seen) or self.inorderTraversal(root.right,k,seen)
        
    
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        return self.inorderTraversal(root,k,seen)
    
    