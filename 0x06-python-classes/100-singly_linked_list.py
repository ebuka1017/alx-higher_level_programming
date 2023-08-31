#!/usr/bin/python3

"""Singly linked list"""


class Node:
    """Initialize node class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """define singly linked list class"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        newList = []

        while(self.__head):
            newList.append(self.__head.data)
            self.__head = self.__head.next_node
        return("\n".join([str(x) for x in sorted(newList)]))

    def sorted_insert(self, value):
        newNode = Node(value, self.__head)
        self.__head = newNode
