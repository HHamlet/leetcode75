# Definition for a binary tree node.
from typing import DefaultDict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ### 1 solution ####
        queue =[root]
        next_q =[]
        level =[]
        output =[]

        if root is None: return []
        while queue !=[]:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_q.append(root.left)
                if root.right is not None:
                    next_q.append(root.right)
            output.append(level)
            level =[]
            queue =next_q
            next_q =[]
        return output
        # ### 2 solution #####
        #  d =DefaultDict(list)    #### / from typing or collections libiary
        #  def dfs(node,level):
        #     if node is None: return
        #     d[level].append(node.val)
        #     dfs(node.left,level+1)
        #     dfs(node.right,level+1)
        
        #  dfs(root,0)
        #  return d.values()



