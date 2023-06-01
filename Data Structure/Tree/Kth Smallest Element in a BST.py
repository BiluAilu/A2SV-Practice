# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=[]
        def help(root):
            if root:
                result.append(root.val)
                help(root.left)
                help(root.right)
        help(root)
        result.sort()
        return result[k-1]

