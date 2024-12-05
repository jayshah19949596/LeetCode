"""
863. All Nodes Distance K in Binary Tree [MEDIUM]
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

### 1. Question Explanation:
----------------------------
Given the root of a binary tree, the value of a target node "target", and an integer "k".
Return an array of the values of all nodes that have a distance k from the target node.

### 2. Solution Explanation:
----------------------------
Intuition: Traverse from target node and see if the children or ancestrol nodes are distanced by value k
Find Path from root to target in path.
For all node in path traverse in dfs fashion to find nodes distanced with value k from target.

Key Ideas:
1. Path finding: First, the path from the root to the target node is determined.
2. DFS search: Starting from the target node, it performs DFS to find nodes that are exactly k distance away.
3. Blockers: When moving up from the target node (along the path), child nodes (blockers) are ignored during further DFS to avoid revisiting nodes.

### 3. Complexity Analysis:
----------------------------
Time Complexity: O(N): for visiting all nodes
Space Complexity: O(N), for maintaining path variable from root to target node.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path, results, blocker = [], [], None
        self.root_target_path(root, target, path) # path[0] = target node and path[-1]=root node
        for i in range(len(path)):
            # blocker is the immediate child node i.e. path[i-1] from current node i.e. path[i]
            if i>0: blocker = path[i-1]
            self.find_nodes_with_k_dist(path[i], k-i, results, blocker) # At current node the kth distance from target node will be (k-i)th distance from current node i.e. path[i]
        return results

    def find_nodes_with_k_dist(self, node, dist, results, blocker):
        if not node or node == blocker or dist<0: return
        if dist == 0: results.append(node.val)
        self.find_nodes_with_k_dist(node.left, dist-1, results, blocker)
        self.find_nodes_with_k_dist(node.right, dist-1, results, blocker)

    def root_target_path(self, node, target, path):
        if not node:
            return False
        if node == target or self.root_target_path(node.left, target, path) or self.root_target_path(node.right, target, path):
            path.append(node)
            return True
        return False
