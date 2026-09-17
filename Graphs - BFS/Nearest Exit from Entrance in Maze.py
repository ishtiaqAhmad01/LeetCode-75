class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        rows = len(maze)-1
        cols = len(maze[0])-1

        def is_border(cordinates):
            
            if 0 in cordinates or rows == cordinates[0] or cols == cordinates[1]:
                return True
            return False

        neabours = [(0, -1), (-1, 0), (0, 1), (1, 0)]


        queue = deque([(entrance, 0)])
        visited = set([tuple(entrance)])

        while queue:
            current = queue.popleft()

            if is_border(current[0]) and current[0] != entrance:
                return current[1]

            for n in neabours:
                new_row, new_col = current[0][0] + n[0], current[0][1] + n[1]

                if 0 <= new_row <= rows and 0 <= new_col <= cols and maze[new_row][new_col] == "." and (new_row, new_col) not in visited:
                    queue.append(([new_row, new_col], current[1]+1))
                    visited.add((new_row, new_col))

        
        return -1






        
