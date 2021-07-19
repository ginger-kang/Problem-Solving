# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def checkTree(curr, height):
            if not curr:
                return 0
            
            # print(curr.val, height)
            
            leftSubTrees = checkTree(curr.left, height + 1)
            rightSubTrees = checkTree(curr.right, height + 1)
            
            # print('left: ', leftSubTrees, 'right: ', rightSubTrees)
            
            if abs(leftSubTrees - rightSubTrees) > 1:
                return float('inf')
            
            return 1 + max(leftSubTrees, rightSubTrees)
        
        return checkTree(root, 0) != float('inf')