# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, roots: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        def insert(root, val):
            if root==None :
               return  TreeNode(val)
                
            elif root.val>value:
                root.left=insert(root.left,val)
            elif root.val<value:
                root.right=insert(root.right,val)
            return root
        
        return insert(roots,value)