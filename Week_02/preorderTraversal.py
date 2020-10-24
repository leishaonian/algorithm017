class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        des = []
        if root:
            des.append(root.val)
            des += self.preorderTraversal(root.left)
            des += self.preorderTraversal(root.right)
        return des
