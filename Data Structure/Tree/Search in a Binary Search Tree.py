# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, roots: Optional[TreeNode], val: int) -> Optional[TreeNode]:
                
        def search(root):
            if root==None:
                return None
            elif root.val==val:
                return root
            elif root.val<val:
                return search(root.right)
            else:
                return search(root.left)
        return search(roots)