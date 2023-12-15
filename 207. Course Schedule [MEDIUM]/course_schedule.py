"""
https://leetcode.com/problems/course-schedule/

### 1. Question Explanation:
----------------------------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

#### Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

#### Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

### 2. Solution Explanation:
----------------------------
APPROACH: Topological Sort Using Kahn's Algorithm
Step-1: Compute in-degree (number of incoming edges) for each of the vertex present in the DAG and initialize the count of visited nodes as 0.
Step-2: Pick all the vertices with in-degree as 0 and add them into a queue (Enqueue operation)
Step-3: Remove a vertex from the queue (Dequeue operation) and then.
        - Increment the count of visited nodes by 1.
        - Decrease in-degree by 1 for all its neighbouring nodes.
        - If the in-degree of neighbouring nodes is reduced to zero, then add it to the queue.
Step-4: Repeat Step 3 until the queue is empty.
Step-5: If the count of visited nodes is not equal to the number of nodes in the graph then the topological sort is not possible for the given graph.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(V+E)
Space Complexity: O(V+E)
"""
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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, incoming_edges, no_of_unique_nodes = Solution.create_graph(prerequisites)
        queue = Solution.get_seed_nodes(graph, incoming_edges)
        num_of_courses_compelted = 0

        while queue:
            cur_node = queue.pop()
            num_of_courses_compelted += 1
            for child_node in graph[cur_node]:
                incoming_edges[child_node] -= 1
                if incoming_edges[child_node] == 0:
                    queue.append(child_node)
            if num_of_courses_compelted > numCourses: return False

        return num_of_courses_compelted == no_of_unique_nodes
