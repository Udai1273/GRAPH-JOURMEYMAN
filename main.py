import time
import networkx as nx
import matplotlib.pyplot as plt
from bellmanford import bellman_ford
from astar import astar
from dijkstra import dijkstra


def draw_graph(G, pos, path=None):
    plt.clf()  # Clear the current figure
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)

    if path:
        edges_in_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='r', width=2.5)

    plt.pause(0.5)  # Pause for a short animation effect


def main():
    # Define a sample graph
    G = nx.Graph()
    G.add_weighted_edges_from([
        (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11),
        (7, 8, 7), (7, 6, 1), (2, 8, 2), (8, 6, 6),
        (2, 3, 7), (2, 5, 4), (6, 5, 2), (3, 5, 14),
        (3, 4, 9), (4, 5, 10)
    ])

    pos = nx.spring_layout(G)  # Position for all nodes
    draw_graph(G, pos)

    source, target = 0, 4

    print("Choose algorithm: 1. Dijkstra 2. Bellman-Ford 3. A*")
    choice = int(input("Enter choice: "))

    start_time = time.time()

    if choice == 1:
        path, dist = dijkstra(G, source, target, draw_func=lambda p: draw_graph(G, pos, p))
    elif choice == 2:
        path, dist = bellman_ford(G, source, target, draw_func=lambda p: draw_graph(G, pos, p))
    elif choice == 3:
        path, dist = astar(G, source, target, draw_func=lambda p: draw_graph(G, pos, p))
    else:
        print("Invalid choice")
        return

    end_time = time.time()

    print(f"Shortest path: {path}")
    print(f"Distance: {dist}")
    print(f"Time taken: {end_time - start_time} seconds")

    plt.show()


if __name__ == "__main__":
    main()
