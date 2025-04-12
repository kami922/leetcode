class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0 
        self.k = k
        self.inorder(root)
        return self.ans
    def inorder(self,node):
        if node.left:
            self.inorder(node.left)
        self.count += 1
        if self.count == self.k:
            self.ans = node.val
            return
        if node.right:
            self.inorder(node.right)

    