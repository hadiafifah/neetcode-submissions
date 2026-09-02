# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        wtf is a level order traersal ohhh i see
        okay so this is definitely bfs.
        do i need to create a new bfs function every time i do this?
        or can i create a queue, 
        """
        result = []
        queue = deque()
        queue.append(root)

        # while we still have children to look at
        while queue:
            level = []
            # for each node in queue
            queue_length = len(queue)
            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    # if node has no child on that side, None gets added to queue
                    # and then is handled in this if
                    queue.append(node.left)
                    queue.append(node.right)
                # make sure you're not appending an empty level
            if level:
                result.append(level)
        return result




        