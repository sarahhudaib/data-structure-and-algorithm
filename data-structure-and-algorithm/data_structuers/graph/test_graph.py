from graph import Graph, Node
import pytest


def test_add_node():
    graph = Graph()
    assert graph.add_node(1).value == 1


def test_add_edges():
    graph = Graph()
    b = graph.add_node('banana')
    a = graph.add_node('apple')
    graph.add_edge(a, b)
    assert graph._adjacency_list[a][0] == (b, 0)
    assert graph.get_neighbors(a) == [(b, 0)]
    graph.add_edge(b, a)
    assert graph.get_neighbors(b) == [(a, 0)]


def test_edge_node_one():
    graph = Graph()
    a = Node('a')
    b = graph.add_node('b')
    with pytest.raises(KeyError):
        graph.add_edge(a, b)


def test_add_edge_weight():
    graph = Graph()
    b = graph.add_node('b')
    a = graph.add_node('apple')
    graph.add_edge(a, b, 10)
    assert graph.get_neighbors(a) == [(b, 10)]
    graph.add_edge(b, a, 20)
    assert graph.get_neighbors(b) == [(a, 20)]


def test_add_edges_nodes_neighbors():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    graph.add_edge(a, b, 1)
    graph.add_edge(a, c, 2)
    graph.add_edge(a, d, 3)

    n = graph.get_neighbors(a)
    assert n[0][0].value == 'b'
    assert n[0][1] == 1
    assert isinstance(n[0][0], Node)
    assert n[1][0].value == 'c'
    assert n[1][1] == 2
    assert isinstance(n[1][0], Node)
    assert n[2][0].value == 'd'
    assert n[2][1] == 3
    assert isinstance(n[2][0], Node)


def test_get_nodes():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    not_included = Node('z')
    assert len(graph.get_nodes()) == 3


def test_get_neighbors():
    graph = Graph()
    a = graph.add_node(100)
    b = graph.add_node(200)
    graph.add_edge(b, a, 10)
    neighbors = graph.get_neighbors(b)
    assert len(neighbors) == 1
    assert neighbors[0][0].value == 100
    assert isinstance(neighbors[0][0], Node)
    assert neighbors[0][1] == 10


def test_size():
    graph = Graph()
    graph.add_node(1)
    assert graph.size() == 1
    graph.add_node(2)
    assert graph.size() == 2
