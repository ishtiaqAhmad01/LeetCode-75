class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        

        ans = 0
        queue = deque([0])
        visited = [False] * n
        visited[0] = True

        while queue:
            curr = queue.popleft()

            for neighbour, cost in graph[curr]:

                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

                    if cost == 1:
                        ans+=1
        return ans 

        
