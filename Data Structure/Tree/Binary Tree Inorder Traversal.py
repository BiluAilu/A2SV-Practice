# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, roots: Optional[TreeNode]) -> List[int]:
        inorder=[]
        def InorderF (root):
            if root:
            # First recur on left child
                InorderF(root.left)
                # then print the data of node
                inorder.append(root.val),
                # now recur on right child
                InorderF(root.right)
        InorderF(roots)
        return inorder
