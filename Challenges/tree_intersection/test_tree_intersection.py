from tree_intersection import *

import pytest

@pytest.fixture
def my_tree1():
    binary_tree = BinaryTree()
    binary_tree.root = Node(10)
    binary_tree.root.right = Node(20)
    binary_tree.root.left = Node(30)
    binary_tree.root.left.left = Node(40)
    binary_tree.root.left.right = Node(50)
    binary_tree.root.left.right.left = Node(60)
    binary_tree.root.left.right.right = Node(70)
    binary_tree.root.right.left = Node(80)
    binary_tree.root.right.right = Node(90)
    binary_tree.root.right.right.left = Node(100)
    return binary_tree

@pytest.fixture
def my_tree2():
    binary_tree1 = BinaryTree()
    binary_tree1.root = Node(101)
    binary_tree1.root.right = Node(20)
    binary_tree1.root.left = Node(301)
    binary_tree1.root.left.left = Node(40)
    binary_tree1.root.left.right = Node(501)
    binary_tree1.root.left.right.left = Node(60)
    binary_tree1.root.left.right.right = Node(701)
    binary_tree1.root.right.left = Node(80)
    binary_tree1.root.right.right = Node(901)
    binary_tree1.root.right.right.left = Node(100)
    return binary_tree1

def test_tree1_tree2_intersection(my_tree1,my_tree2):
    actual = tree_intersection(my_tree1,my_tree2)
    expect = {100, 40, 80, 20, 60}
    assert actual == expect

def test_empty_tree():
    bt = BinaryTree()
    bt1 = BinaryTree()
    actual = tree_intersection(bt,bt1)
    expect = 'This tree is empty'
    assert actual == expect


def test_simply_tree_case(my_tree1, my_tree2):
    tree1 = my_tree1
    tree2 = my_tree2
    assert tree_intersection(tree1, tree2) == {100, 40, 80, 20, 60}





