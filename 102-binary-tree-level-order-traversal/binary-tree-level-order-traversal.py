# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        q = collections.deque()
        q.append(root)
        while q:
            same_level_nodes = []
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                same_level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(same_level_nodes)
        return res            
        