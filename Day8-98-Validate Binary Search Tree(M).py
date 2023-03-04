# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def BSTvalid(root,lowwer,upper):
            if root is None:
                return True
            if root.val <= lowwer or root.val >= upper:
                return False
            else:
                return BSTvalid(root.left,lowwer,root.val) and BSTvalid(root.right,root.val,upper)
        return BSTvalid(root,float("-inf"),float("inf"))
