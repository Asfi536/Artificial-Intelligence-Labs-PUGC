class CustomStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

class Network:
    def __init__(self):
        self.connections = {}

    def connect_nodes(self, vertex, edge):
        if vertex not in self.connections:
            self.connections[vertex] = set()

        if edge not in self.connections:
            self.connections[edge] = set()
        self.connections[vertex].add(edge)
        self.connections[edge].add(vertex)

    def depth_first_search(self, start_node, target_node):
        stack = CustomStack()
        visited = set()

        stack.push(start_node)
        visited.add(start_node)

        while not stack.is_empty():
            current_node = stack.pop()
            print(current_node, end=" ")

            if current_node == target_node:
                print("\nTarget node found")
                return

            for neighbor in self.connections[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)

        print("\nTarget node not found")
        return

network_data = {
    'A': {'B', 'H', 'I'},
    'B': {'C', 'G'},
    'C': {'D', 'E'},
    'D': {},
    'E': {},
    'G': {},
    'H': {},
    'I': {'J', 'M'},
    'J': {'K', 'L'},
    'K': {},
    'L': {},
    'M': {}
}

network = Network()
for vertex, edges in network_data.items():
    for edge in edges:
        network.connect_nodes(vertex, edge)

network.depth_first_search('E', 'L')
