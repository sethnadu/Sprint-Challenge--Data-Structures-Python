from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            # Add item as node to tail
            self.storage.add_to_tail(item)
            # Keep track of current head
            self.current = self.storage.head
        else:
            # Set current head value to item
            self.current.value = item
            # set current to be current.next (self.storage.head.next)
            self.current = self.current.next
            # If current.next is none, reset current to head again
            if self.current.next is None:
                self.current.next = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
         # TODO: Your code here
        node = self.storage.head
        while node is not self.storage.tail:
            list_buffer_contents.append(node.value)
            node = node.next
        list_buffer_contents.append(self.storage.tail.value)
        # print(list_buffer_contents)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


# buffer = RingBuffer(5)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e')
# buffer.append('f')
# buffer.append('g')
# buffer.append('h')
# buffer.append('i')
# buffer.append('j')
# buffer.append('k')


# buffer.get()