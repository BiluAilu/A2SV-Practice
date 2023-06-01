# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successor(root):
            current=root
            while current.left:
                current=current.left
            return current
        if root==None:
            return root
        if key> root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left=self.deleteNode(root.left, key)
        else:
            if root.left==None :
                return root.right
            elif root.right==None:
                return root.left
            
            temp=successor(root.right)

            root.val=temp.val

            root.right=self.deleteNode(root.right, temp.val)
        return root

        