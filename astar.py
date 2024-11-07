import heapq
import math
import networkx as nx


def heuristic(node, target, pos):
    # Heuristic: Euclidean distance (or straight-line distance)
    x1, y1 = pos[node]
    x2, y2 = pos[target]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def astar(graph, start, target, draw_func=None):
    pos = nx.spring_layout(graph)
    queue = [(0, start, [])]
    seen = set()
    g_score = {start: 0}
    f_score = {start: heuristic(start, target, pos)}

    while queue:
        (cost, node, path) = heapq.heappop(queue)

        if node in seen:
            continue

        path = path + [node]
        seen.add(node)

        if node == target:
            if draw_func:
                draw_func(path)
            return path, g_score[target]

        for neighbor, weight in graph[node].items():
            tentative_g_score = g_score[node] + weight['weight']
            if neighbor in seen and tentative_g_score >= g_score.get(neighbor, float('inf')):
                continue

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, target, pos)
                heapq.heappush(queue, (f_score[neighbor], neighbor, path))
                if draw_func:
                    draw_func(path + [neighbor])

    return [], float('inf')
