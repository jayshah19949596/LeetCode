"""
133. Clone Graph [MEDIUM]
https://leetcode.com/problems/clone-graph

### 1. Question:
----------------------------
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

### 2. Solution:
----------------------------
Iterative DFS

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(V+E), V is a number of nodes (vertices) and E is a number of edges
Space Complexity: O(V)
"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        visited = {node: Node(node.val)}
        stack = [node]

        while stack:
            cur_node = stack.pop()
            cur_copy_node = visited[cur_node]
            cur_copy_node_neighbor_list = []

            for neighbor_node in cur_node.neighbors:
                if neighbor_node not in visited:
                    copy_neighbor_node = Node(neighbor_node.val)
                    visited[neighbor_node] = copy_neighbor_node
                    stack.append(neighbor_node)
                cur_copy_node_neighbor_list.append(visited[neighbor_node])
            cur_copy_node.neighbors = cur_copy_node_neighbor_list

        return visited[node]
