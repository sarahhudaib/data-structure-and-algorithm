# Implementation: Graph
Author: Sarah Hudaib


## Challenge
Implement the graph, which should be represented as an adjacency list, and should include the following methods: add_node(), add_edge(), get_nodes(), get_neighbors(), size()

## Approach & Efficiency
- add_node() time Big O(1), space Big O(1)
- add_edge() time Big O(1), space Big O(1)
- get_nodes() time Big O(1), space Big O(1)
- get_neighbors() time Big O(1), space Big O(1)
- size() time Big O(1), space Big O(1)

## API
- class Vertex():

    - Class to create Vertex with the given value
    - Input: Vertex value

- class Graph():
    - class to implement Graph object with the given methods:

    - add_node():

        Adds a new vertex to the graph
        - Input: the value of that vertex
        - Output: the added vertex
    - add_edge():

        Adds a new edge between two nodes in the graph with ability to add weight
        - Input: two vertexes to be connected by the edge
        - Both nodes should already be in the Graph
    - get_nodes():

        Returns all of the vertexes in the graph as a collection
    - get_neighbors():

        Returns a collection of vertexes connected to the given vertex with the weights of their connections
        - Input: Takes in a given vertex
    - size():

        Returns the total number of nodes in the graph

## Code
[Link](./graph.py) 

## Tests
[Link](./test_graph.py) 