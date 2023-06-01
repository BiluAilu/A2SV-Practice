# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder.reverse()
        def help(left,right):
            if left>right:
                return 
            node=preorder.pop()
            index=inorder.index(node)
            root=TreeNode(node)
            root.left=help(left,index-1)
            root.right=help(index+1,right)

            return root
        
        return help(0,len(preorder)-1)
