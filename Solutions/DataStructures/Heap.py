from typing import Union


def get_parent_position(position: int) -> int:
    # helper function get the position of the parent of the current node
    return (position - 1) // 2


def get_left_child_position(position: int) -> int:
    # helper function get the position of the left child of the current node
    return (2 * position) + 1


def get_right_child_position(position: int) -> int:
    # helper function get the position of the right child of the current node
    return (2 * position) + 2


class MinHeap:
    """
    Min Heap class

    Functions:
    extract_min: Remove and return the minimum element from the heap
    insert: Insert a node into the heap
    peek: Get the minimum element from the heap
    _bubble_up: helper function to place a node at the proper position (upward
                movement)
    _bubble_down: helper function to place a node at the proper position (downward
                movement)
    _swap_nodes: helper function to swap the nodes at the given positions
    """

    def __init__(self) -> None:
        self.heap = []
        self.elements = 0

    def __len__(self) -> int:
        return self.elements

    def __repr__(self) -> str:
        return str(self.heap)

    def extract_min(self) -> Union[int, str]:
        # function to remove and return the minimum element from the heap
        if self.elements == 0:
            raise RuntimeError("Heap Underflow. Cannot extract min from a empty heap")

        if self.elements > 1:
            self._swap_nodes(0, self.elements - 1)
        elem = self.heap.pop()
        self.elements -= 1
        if self.elements > 0:
            self._bubble_down(0)
        return elem

    def insert(self, elem: Union[int, str]) -> None:
        # function to insert a node into the heap
        self.heap.append(elem)
        self._bubble_up(self.elements)
        self.elements += 1

    def peek_min(self) -> Union[int, str]:
        # function to get the minimum element from the heap
        if self.elements == 0:
            raise RuntimeError("Heap is empty")
        return self.heap[0]

    def _bubble_up(self, curr_pos: int) -> None:
        # Place a node at the proper position (upward movement) [to be used internally
        # only]
        if curr_pos == 0:
            return
        parent_position = get_parent_position(curr_pos)
        elem = self.heap[curr_pos]
        parent = self.heap[parent_position]
        if parent > elem:
            self._swap_nodes(parent_position, curr_pos)
            self._bubble_up(parent_position)

    def _bubble_down(self, curr_pos: int) -> None:
        # Place a node at the proper position (downward movement) [to be used
        # internally only]
        elem = self.heap[curr_pos]
        child_left_position = get_left_child_position(curr_pos)
        child_right_position = get_right_child_position(curr_pos)
        if child_left_position < self.elements and child_right_position < self.elements:
            child_left = self.heap[child_left_position]
            child_right = self.heap[child_right_position]
            if child_right < child_left:
                if child_right < elem:
                    self._swap_nodes(child_right_position, curr_pos)
                    return self._bubble_down(child_right_position)
        if child_left_position < self.elements:
            child_left = self.heap[child_left_position]
            if child_left < elem:
                self._swap_nodes(child_left_position, curr_pos)
                return self._bubble_down(child_left_position)
        else:
            return
        if child_right_position < self.elements:
            child_right = self.heap[child_right_position]
            if child_right < elem:
                self._swap_nodes(child_right_position, curr_pos)
                return self._bubble_down(child_right_position)

    def _swap_nodes(self, pos1: int, pos2: int) -> None:
        # function to swap two nodes in the heap [to be used internally only]
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]


class MaxHeap:
    """
    Max Heap class

    Functions:
    extract_max: Remove and return the maximum element from the heap
    insert: Insert a node into the heap
    peek: Get the maximum element from the heap
    _bubble_up: helper function to place a node at the proper position (upward
                movement)
    _bubble_down: helper function to place a node at the proper position (downward
                movement)
    _swap_nodes: helper function to swap the nodes at the given positions
    """

    def __init__(self) -> None:
        self.heap = []
        self.elements = 0

    def __len__(self) -> int:
        return self.elements

    def __repr__(self) -> str:
        return str(self.heap)

    def extract_max(self) -> Union[int, str]:
        # function to remove and return the minimum element from the heap
        if self.elements == 0:
            raise RuntimeError("Heap Underflow. Cannot extract max from a empty heap")

        if self.elements > 1:
            self._swap_nodes(0, self.elements - 1)
        elem = self.heap.pop()
        self.elements -= 1
        if self.elements > 0:
            self._bubble_down(0)
        return elem

    def insert(self, elem: Union[int, str]) -> None:
        # function to insert a node into the heap
        self.heap.append(elem)
        self._bubble_up(self.elements)
        self.elements += 1

    def peek_max(self) -> Union[int, str]:
        # function to get the minimum element from the heap
        if self.elements == 0:
            raise RuntimeError("Heap is empty")
        return self.heap[0]

    def _bubble_up(self, curr_pos: int) -> None:
        # Place a node at the proper position (upward movement) [to be used internally
        # only]
        if curr_pos == 0:
            return
        parent_position = get_parent_position(curr_pos)
        elem = self.heap[curr_pos]
        parent = self.heap[parent_position]
        if parent < elem:
            self._swap_nodes(parent_position, curr_pos)
            self._bubble_up(parent_position)

    def _bubble_down(self, curr_pos: int) -> None:
        # Place a node at the proper position (downward movement) [to be used
        # internally only]
        elem = self.heap[curr_pos]
        child_left_position = get_left_child_position(curr_pos)
        child_right_position = get_right_child_position(curr_pos)
        if child_left_position < self.elements and child_right_position < self.elements:
            child_left = self.heap[child_left_position]
            child_right = self.heap[child_right_position]
            if child_right > child_left:
                if child_right > elem:
                    self._swap_nodes(child_right_position, curr_pos)
                    return self._bubble_down(child_right_position)
        if child_left_position < self.elements:
            child_left = self.heap[child_left_position]
            if child_left > elem:
                self._swap_nodes(child_left_position, curr_pos)
                return self._bubble_down(child_left_position)
        else:
            return
        if child_right_position < self.elements:
            child_right = self.heap[child_right_position]
            if child_right > elem:
                self._swap_nodes(child_right_position, curr_pos)
                return self._bubble_down(child_right_position)

    def _swap_nodes(self, pos1: int, pos2: int) -> None:
        # function to swap two nodes in the heap [to be used internally only]
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]
