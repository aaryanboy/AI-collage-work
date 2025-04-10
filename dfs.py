def dfsDemo(graph, start_node, goal_node):
    stack = [(start_node, [start_node])]
    visited_order = []

    while stack:
        current_node, path = stack.pop()

        if current_node not in visited_order:
            visited_order.append(current_node)
            print("Path traversed:", "{" + ",".join(visited_order) + "}")

            if current_node == goal_node:
                return path

            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited_order:
                    stack.append((neighbor, path + [neighbor]))

    return None


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': ['I', 'J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

start = 'A'
goal = 'J'
path = dfsDemo(graph, start, goal)

print("")
if path:
    print("Path from", start, "to", goal, ":", path)
else:
    print("No path found from", start, "to", goal)