from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = dict.fromkeys(range(n), False)
        visited[0] = True

        queue = deque(rooms[0])

        while queue:
            curr = queue.popleft()
            # print(curr, queue)
            if not visited[curr]:
                queue.extend(rooms[curr])
                visited[curr] = True
            

        # print(visited)
        return not False in visited.values()
