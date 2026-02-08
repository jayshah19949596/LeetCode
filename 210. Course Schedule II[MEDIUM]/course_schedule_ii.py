from collections import defaultdict, deque


class Solution:
    @staticmethod
    def create_graph(prerequisites):
        graph = defaultdict(list)
        incoming_edges = defaultdict(int)
        unique_nodes = set([])
        for prerequisite in prerequisites:
            start, end = prerequisite[1], prerequisite[0]
            graph[start].append(end)
            incoming_edges[end] += 1
            unique_nodes.add(start), unique_nodes.add(end)
        return graph, incoming_edges, len(unique_nodes)

    @staticmethod
    def get_seed_nodes(graph, incoming_edges):
        queue = deque()
        for node in graph:
            if incoming_edges[node] == 0:
                queue.appendleft(node)
        return queue

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1 and not prerequisites: return [0] 
        graph, incoming_edges, no_of_unique_nodes = Solution.create_graph(prerequisites)
        queue = Solution.get_seed_nodes(graph, incoming_edges)
        num_of_courses_compelted = 0
        order = [] 
        while queue:
            cur_node = queue.pop()
            order.append(cur_node)
            num_of_courses_compelted += 1
            for child_node in graph[cur_node]:
                incoming_edges[child_node] -= 1
                if incoming_edges[child_node] == 0:
                    queue.append(child_node)

        return order if len(order) == numCourses else []

        
