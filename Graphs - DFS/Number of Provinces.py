from collections import deque
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * len(isConnected)

        # adj matrix to adj list
        graph = {}

        for i in range(n):
            current_row = []
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    current_row.append(j+1)
            graph[i+1] = current_row


        def traverse(node):
            queue = deque([node])
            visited[node-1] = True

            while queue:
                curr = queue.popleft()

                for neighbour in graph[curr]:
                    if not visited[neighbour-1]:
                        queue.append(neighbour)
                        visited[neighbour-1] = True


        ans = 0
        for i in range(n):
            if not visited[i]:
                traverse(i+1)
                ans+=1
        return ans











