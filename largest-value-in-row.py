'''
Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(n) for the queue
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        output = []
        queue = deque()

        def bfs(queue: Deque): 
            length = len(queue) 
            if length==0:
                return 
            largest = float("-inf")
            while length > 0:
                node = queue.popleft()
                largest = max(largest, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                length -= 1
            output.append(largest)
            bfs(queue)

        if root:
            queue.append(root)
            bfs(queue)
        return output
