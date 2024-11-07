import heapq


def dijkstra(graph, start, target, draw_func=None):
    queue = [(0, start, [])]
    seen = set()
    min_dist = {start: 0}

    while queue:
        (cost, node, path) = heapq.heappop(queue)

        if node in seen:
            continue

        path = path + [node]
        seen.add(node)

        if node == target:
            if draw_func:
                draw_func(path)  # Visualization
            return path, cost

        for neighbor, weight in graph[node].items():
            if neighbor in seen:
                continue
            prev = min_dist.get(neighbor, float('inf'))
            next_dist = cost + weight['weight']
            if next_dist < prev:
                min_dist[neighbor] = next_dist
                heapq.heappush(queue, (next_dist, neighbor, path))
                if draw_func:
                    draw_func(path + [neighbor])

    return [], float('inf')
