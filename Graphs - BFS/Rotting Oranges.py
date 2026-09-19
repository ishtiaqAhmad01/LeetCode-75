class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def isvalid_position(position):
            if 0 <= position[0] < m and 0 <= position[1] < n and grid[position[0]][position[1]] == 1:
                return True
            return False

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append(((i,j), 0))
                    
        ans = 0
        while queue:
            current = queue.popleft()

            ans = max(ans, current[1])

            directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            for direction in directions:
                new_position = current[0][0] + direction[0], current[0][1] + direction[1]

                if isvalid_position(new_position):
                    queue.append((new_position, current[1]+1))
                    grid[new_position[0]][new_position[1]] = 2

        for row in grid:
            if 1 in row:
                return -1
        
        return ans
