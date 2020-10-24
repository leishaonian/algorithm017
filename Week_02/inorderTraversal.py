class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res =[]
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res
