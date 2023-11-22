#!/usr/bin/python3
"""The task requires you to define two classes, Node and SinglyLinkedList,
to implement a singly linked list. The Node class represents a node in the
linked list, and the SinglyLinkedList class represents the linked list
itself. The Node class has private instance attributes data and next_node,
along with their respective getters and setters. The SinglyLinkedList class
has a private instance attribute head and methods to insert a new node into
the sorted position and print the linked list. Start by defining the Node
class with private attributes data and next_node"""


class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
        """Implement getters and setters for the data attribute"""
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
        """Implement getters and setters for the next_node attribute"""
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
        """Define the SinglyLinkedList class with a private
        instance attribute head"""


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        """Implement the sorted_insert method to insert a new node into
        the correct sorted position"""
    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None \
                    and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
            """Implement the __str__ method to provide a string
            representation of the linked list"""
    def __str__(self):
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
