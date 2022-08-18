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
        

# Balanced Binary Tree (110)
# Time: O(n)
def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # dfs through the tree
        # keeping track of isBalanced bool and height
        def dfs(root):
            if not root:
                return [True, -1]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return [balanced, 1 + max(left[1], right[1])]
            
        return dfs(root)[0]
        
   
# Same Tree (100)
# Time: O(n)
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
	
	# Reached the end and return true
        if not q and not p:
            return True
            
        # Return false if values diff or one of them is null
        if (not q or not p) or (p.val != q.val):
            return False
        
        # If true continue iterating through the tree
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
                

# Subtree of another tree (572)
# Time: O(r*s)    
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Checks the edge cases
        # If subroot is null auto return True
        if not subRoot:
            return True
        
        # If root is null auto return False
        if not root:
            return False
        
        # Run isSametree to see if subroot == root
        if self.isSameTree(root, subRoot):
            return True
        
        # Call the function with root's left and right children if not the same tree
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
                

# Lowest Common Ancestor (235)
# Time: O(n)
# Basic Approach: Utilize the structure of a binary search tree
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        # Trying to find the split(middle value of 'p' and 'q')
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            
            else:
                return curr
                

# Binary Tree Level Order Traversal (102)
# Time: O(n)
# Definition of BFS (Breadth First Search)
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = []
        
        while q:
            if not root:
                return res
            flag = []
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                flag.append(node.val)
            
            res.append(flag)
        
        return res
        
   
# Validate Binary Search Tree (98)
# Time: O(n)
# Basic Approach: Use DFS and update left and right boundaries
def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            if node.val <= left:
                return False
            if node.val >= right:
                return False
            
            return (dfs(node.left, left, node.val) and
                    dfs(node.right, node.val, right))
            
                
        return dfs(root, float("-inf"), float("inf"))
        

# Kth Smallest Element in BST (230)   
# Time: O(n)
# Approach: Build a queue using In-Order Traversal Technique and return the value at that index  
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        
        def dfs(root):
            if not root:
                return
            curr = root
            
            if curr.left:
                dfs(curr.left)
            
            q.append(curr.val)
            if curr.right:
                dfs(curr.right)
            
        dfs(root)
        return q[k - 1]
        

# Construct Binary Tree from Preorder and Inorder Traversal (105)
# Time: O(n)
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        

# Construct Binary Tree from Preorder and Inorder Traversal        
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
