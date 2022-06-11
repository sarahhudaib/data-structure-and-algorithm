class Node:
    def __init__(self, value):
        self.value = value
        # self.edges = []

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """ method to add a node to the graph   
                Args:   value: the value of the node
                Returns: None
        """
        vertex = Node(value)

        self._adjacency_list[vertex] = []
        return vertex

    def size(self):
        """method to return the size of the graph
                Args:   None    
                Returns: the size of the graph
        """
        return len(self._adjacency_list)

    def add_edge(self, vertex1, vertex2, weight=0):
        """ method to add an edge to the graph  
                Args:   start_vertex: the starting vertex of the edge
                        end_vertex: the ending vertex of the edge
                        weight: the weight of the edge
                Returns: None
        """

        if vertex1 not in self._adjacency_list:
            raise KeyError('Start & End Vertices are not in the Graph')

        if vertex2 not in self._adjacency_list:
            raise KeyError('End Vertex not in Graph')

        adjacencies = self._adjacency_list[vertex1]
        adjacencies.append((vertex2, weight))

    def get_nodes(self):
        """method to return the nodes of the graph  
                Args:   None
                Returns: the nodes of the graph
        """
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """method to return the neighbors of a vertex
                Args:   vertex: the vertex to get the neighbors of
                Returns: the neighbors of the vertex
        """

        return self._adjacency_list[vertex]
    
    def print_graph(self, graph):
        """method to print the graph               
                Args:   None
                Returns: None
        """
        for node in graph:
            print(node.value)
            for neighbor in graph[node]:
                print(neighbor)


if __name__ == '__main__':
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    
    graph.print_graph(graph)
    
    print(graph.size())
    
    print(graph.get_neighbors(1))
    print(graph.get_neighbors(2))
    print(graph.get_neighbors(3))
    
    print(graph.get_edge())
    print(graph.get_node())
    
    print(graph.get_edge_graph())
    print(graph.get_node_graph())
