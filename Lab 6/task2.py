class CustomStack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.elements.pop()

    def is_empty(self):
        return len(self.elements) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.elements[-1]

class NetworkGraph:
    def __init__(self):
        self.connections = {}

    def add_connection(self, vertex, edge):
        if vertex not in self.connections:
            self.connections[vertex] = set()

        if edge not in self.connections:
            self.connections[edge] = set()
        self.connections[vertex].add(edge)
        self.connections[edge].add(vertex)

    def depth_first_search(self, start_vertex, target_vertex):
        stack = CustomStack()
        visited = set()

        stack.push(start_vertex)
        visited.add(start_vertex)

        while not stack.is_empty():
            current_vertex = stack.pop()
            print(current_vertex, end=" ")

            if current_vertex == target_vertex:
                print("\nTarget found")
                return

            for neighbor in self.connections[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.push(neighbor)

        print("\nTarget not found")
        return

network_data = {
    'X': {'Y', 'V', 'Z', 'W'},
    'Y': {'M', 'L'},
    'Z': {},
    'V': {'P'},
    'W': {'Q', 'R', 'S'},
    'P': {},
    'Q': {},
    'R': {},
    'S': {'N'},
    'L': {},
    'M': {'O', 'T'},
    'N': {},
    'O': {},
    'T': {}
}

network = NetworkGraph()
for vertex, edges in network_data.items():
    for edge in edges:
        network.add_connection(vertex, edge)

network.depth_first_search('X', 'P')
