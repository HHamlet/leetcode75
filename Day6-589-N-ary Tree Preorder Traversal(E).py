# Definition for a Node.
from typing import Deque, List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
       
       ## Recursive method####
        # output = []
        # def fs(root):
        #     if root == None: return 
        #     output.append(root.val)
        #     for i in root.children:
        #         fs(i)
        # fs(root)
        # return output
## liniar method (not recursive :)) )####
        q =Deque([root])
        output =[]

        while q:
            cand =q.popleft()
            output.append(cand.val)
            for i in reversed(cand.children):
                q.appendleft(i)
        return output
        