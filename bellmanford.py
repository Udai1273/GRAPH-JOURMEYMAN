def bellman_ford(graph, start, target, draw_func=None):
    dist = {node: float('inf') for node in graph.nodes()}
    dist[start] = 0
    predecessor = {node: None for node in graph.nodes()}

    # Relax edges up to |V| - 1 times
    for _ in range(len(graph.nodes()) - 1):
        for u, v, weight in graph.edges(data=True):
            if dist[u] + weight['weight'] < dist[v]:
                dist[v] = dist[u] + weight['weight']
                predecessor[v] = u
                if draw_func:
                    draw_func([start] + trace_path(predecessor, v))

    # Check for negative weight cycles
    for u, v, weight in graph.edges(data=True):
        if dist[u] + weight['weight'] < dist[v]:
            print("Graph contains a negative weight cycle")
            return [], float('inf')

    return trace_path(predecessor, target), dist[target]


def trace_path(predecessor, node):
    path = []
    while node is not None:
        path.append(node)
        node = predecessor[node]
    return path[::-1]
