# Number of Islands (200)
# Link: https://leetcode.com/problems/number-of-islands/
def numIslands(self, grid: List[List[str]]) -> int:
        # if empty grid
        if not grid:
            return 0
        
        # get dimensions of grid
        rows, cols = len(grid), len(grid[0])
        
        # initialize set to keep up with land visited
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = deque()
            
            # mark as visited
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                # utilize bfs and mark every land connected as visited
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    # check if it's within the range
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and 
                        (r, c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
        
        # need to go through each item in grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
