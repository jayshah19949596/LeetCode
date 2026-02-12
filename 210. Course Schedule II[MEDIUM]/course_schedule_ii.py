from typing import List
from collections import defaultdict, deque


class Solution:
    @staticmethod
    def create_graph(prerequisites, numCourses):
        graph = defaultdict(list)          # same as prereq_list
        incoming_edges = defaultdict(int)  # same as nb_prerequisites

        # Initialize all courses to ensure isolated nodes are included
        for course in range(numCourses):
            incoming_edges[course] = 0

        for after, before in prerequisites:
            graph[before].append(after)
            incoming_edges[after] += 1

        return graph, incoming_edges

    @staticmethod
    def get_seed_nodes(incoming_edges):
        queue = deque()
        for course, count in incoming_edges.items():
            if count == 0:
                queue.append(course)
        return queue

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph, incoming_edges = Solution.create_graph(prerequisites, numCourses)
        queue = Solution.get_seed_nodes(incoming_edges)

        order = []

        while queue:
            cur_node = queue.popleft()
            order.append(cur_node)

            for child_node in graph[cur_node]:
                incoming_edges[child_node] -= 1
                if incoming_edges[child_node] == 0:
                    queue.append(child_node)

        return order if len(order) == numCourses else []
