class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        graph = defaultdict(list)

        for equ, val in zip(equations, values):
            graph[equ[0]].append((equ[1], val))
            graph[equ[1]].append((equ[0], 1/val))
        

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            
            queue = deque([(start, 1)])

            visited = {}
            for key in graph:
                visited[key] = False

            visited[start] = True

            while queue:
                curr_node = queue.popleft()

                if curr_node[0] == end:
                    return curr_node[1]

                for neibour in graph[curr_node[0]]:
                    if not visited[neibour[0]]:
                        visited[neibour[0]] = True
                        queue.append((neibour[0], neibour[1] * curr_node[1]))
            
            return -1.0

        
        ans = []

        for query in queries:
            ans.append(bfs(*query))

        return ans






                


        
