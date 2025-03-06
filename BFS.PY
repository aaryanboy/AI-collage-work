from collections import deque
def bfs(graph , start_node, goal_node):
    queue = deque([(start_node, [start_node])])
    visited = set()
    while queue:
        
