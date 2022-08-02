# RECURSIVE DFS (104)
def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ITERATIVE DFS (104)
def maxDepth1(self, root: Treenode) -> int:
	stack = [[root, 1]]
	res = 0
	
	while stack:
		node, depth = stack.pop()
		
		if node:
			res = max(res, depth)
			stack.append([node.left, depth + 1])
			stack.append([node.right, depth + 1])
	return res


# ITERATIVE BFS (104)
def maxDepth2(self, root: Treenode) -> int:
	if not root:
		return 0
	
	level = 0
	q = deque([root])
	while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


# Diameter of Binary Tree (543)
# Time : O(n)
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Setup global variable
        res = [0]
        
        
        # Setup recursive DFS 
        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Alg that calculates diameter
            res[0] = max(res[0], 2 + left + right)
            
            # Returns the height of the current node
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]
