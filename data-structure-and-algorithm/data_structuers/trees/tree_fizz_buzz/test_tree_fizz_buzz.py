from tree_fizz_buzz import Node, BinaryTree, tree_fizz_buzz

import pytest


def test_fizz_buzz_tree(FizzBuzz):
    """This function is used to test the fizz_buzz function in the tree_fizz_buzz.py"""
    updated_tree = tree_fizz_buzz(FizzBuzz)
    assert updated_tree.root.value == 'Fizz'
    assert updated_tree.root.left.value == 'Buzz'
    assert updated_tree.root.right.value == '7'
    assert updated_tree.root.left.left.value == 'FizzBuzz'


@pytest.fixture
def FizzBuzz():
    """This function is used to create a tree with the value of the node according to fizz_buzz"""
    FizzBuzzTree = BinaryTree()
    FizzBuzzTree.root = Node(3)
    FizzBuzzTree.root.left = Node(5)
    FizzBuzzTree.root.right = Node(7)
    FizzBuzzTree.root.left.left = Node(15)
    return FizzBuzzTree
