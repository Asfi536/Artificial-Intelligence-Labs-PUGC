from collections import deque

class Network:
    def __init__(self):
        self.network = {}

    def connect_nodes(self, source, destination):
        if source not in self.network:
            self.network[source] = []
        if destination not in self.network:
            self.network[destination] = []
        self.network[source].append(destination)

    def bfs_traversal(self, start_point, target):
        explored = set()
        to_visit = deque([start_point])

        explored.add(start_point)

        while to_visit:
            current = to_visit.popleft()
            print(current, end=" ")

            if current == target:
                print("\nTarget reached")
                return

            for adjacent in self.network[current]:
                if adjacent not in explored:
                    explored.add(adjacent)
                    to_visit.append(adjacent)

        print("\nTarget not reached")
        return

dataNetwork = {
    'A': {'B', 'E'},
    'B': {'A', 'C', 'D', 'E'},
    'C': {'B', 'D'},
    'D': {'B', 'C', 'E'},
    'E': {'A', 'B', 'D'}
}

network = Network()

for source, destinations in dataNetwork.items():
    for destination in destinations:
        network.connect_nodes(source, destination)
        
network.bfs_traversal('A', 'D')
