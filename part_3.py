import heapq


class Graph:
    """
    Клас для представлення зваженого графа.
    """

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        """
        Додає вершину в граф.
        """
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2, weight):
        """
        Додає ребро між двома вершинами з вагою.
        """
        self.nodes[node1].append((node2, weight))
        self.nodes[node2].append((node1, weight))  # Для неорієнтованого графа

    def dijkstra(self, start):
        """
        Алгоритм Дейкстри для знаходження найкоротших шляхів від стартової вершини.
        """
        distances = {node: float("inf") for node in self.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.nodes[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Приклад використання
graph = Graph()
for node in ["A", "B", "C", "D", "E"]:
    graph.add_node(node)

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 3)
graph.add_edge("B", "D", 2)
graph.add_edge("C", "D", 4)
graph.add_edge("D", "E", 1)

distances = graph.dijkstra("A")
print("Найкоротші шляхи від вершини A:", distances)
