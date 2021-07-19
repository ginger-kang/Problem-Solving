# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(curr, result):
            # print(curr, result)
            if not curr:
                return
            if curr.val <= high and curr.val >= low:
                result.append(curr.val)
            dfs(curr.left, result)
            dfs(curr.right, result)
        
        result = []
        dfs(root, result)
        return sum(result)