class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            from_node, to_node = edge
            graph[from_node].append(to_node)
            graph[to_node].append(from_node)
        
        queue = deque([source])
        visited = set([source]) # Mark visited when enqueuing
        while queue:
            cur_node = queue.pop()
            if cur_node == destination: return True
            
            for connection in graph[cur_node]:
                if connection not in visited:
                    visited.add(connection)
                    queue.appendleft(connection)

        return False
