from collections import deque

class NetworkGraph:
    def __init__(self):
        self.network = {}

    def add_connection(self, vertex, edge):
        if vertex not in self.network:
            self.network[vertex] = []
        if edge not in self.network:
            self.network[edge] = []
        self.network[vertex].append(edge)

    def bfs_search(self, start_vertex, target_vertex):
        discovered = set()
        search_queue = deque([start_vertex])

        discovered.add(start_vertex)

        while search_queue:
            current_vertex = search_queue.popleft()
            print(current_vertex, end=" ")

            if current_vertex == target_vertex:
                print("\nTarget found")
                return

            for adjacent_vertex in self.network[current_vertex]:
                if adjacent_vertex not in discovered:
                    discovered.add(adjacent_vertex)
                    search_queue.append(adjacent_vertex)

        print("\nTarget not found")
        return

network_data = {
    'X': {'Y', 'Z', 'W'},
    'Y': {'P', 'Q'},
    'Z': {'R'},
    'W': {},
    'P': {},
    'Q': {},
    'R': {}
}

network_graph = NetworkGraph()
for vertex, edges in network_data.items():
    for edge in edges:
        network_graph.add_connection(vertex, edge)

network_graph.bfs_search('X', 'R')
