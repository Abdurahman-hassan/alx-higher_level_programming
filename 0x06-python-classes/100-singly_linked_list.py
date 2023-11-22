#!/usr/bin/python3

"""This module defines a Node class"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the node

        Args:
            data (int): data of the node
            next_node (Node): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes the singly linked list"""
        self.__head = None

    def __str__(self):
        """Prints the singly linked list"""
        string = ""
        node = self.__head
        while node is not None:
            string += str(node.data)
            if node.next_node is not None:
                string += "\n"
            node = node.next_node
        return string

    def sorted_insert(self, value):
        """Inserts a node in a sorted singly linked list"""
        node = self.__head
        if node is None:
            self.__head = Node(value)
            return
        if value < node.data:
            self.__head = Node(value, node)
            return
        while node.next_node is not None:
            if value < node.next_node.data:
                node.next_node = Node(value, node.next_node)
                return
            node = node.next_node
        node.next_node = Node(value)
