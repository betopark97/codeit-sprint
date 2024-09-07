from typing import Any


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
        self.length = 0
        
        
    # Insertion Methods
    def append(self, data):
        # Adds a new node with the given value to the end of the list.
        new_node = Node(data)
        
        if self.length == 0:
            self.head = new_node
        
        if self.length != 0:
            self.tail.next = new_node
        
        self.tail = new_node
        
        self.length += 1
    
    
    def prepend(self, data):
        # Adds a new node with the given value to the beginning of the list.
        new_node = Node(data, self.head)
        
        self.head = new_node
        
        self.length += 1
    
    
    def insert_after(self, node_data, data):
        # Inserts a new node with the given value after a specified node in the list.
        current_node = self.head
        for _ in range(self.length):
            if current_node.data == node_data:
                new_node = Node(data, current_node.next)
                current_node.next = new_node
                self.tail = new_node
                self.length += 1
                return
            current_node = current_node.next
            
        print(f"There is no {node_data} in the linked list.")
    
        
    # Deletion Methods
    def delete(self, data):
        # Removes the first node with the specified value from the list.
        
        # if delete is head
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
            
        current_node = self.head
        for _ in range(self.length):
            # if delete is tail
            if current_node.next.data == data and current_node.next == self.tail:
                current_node.next = None
                self.tail = current_node
                self.length -= 1
                return
            # if delete is in the middle
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                self.length -= 1
                return
            
            # if not the above, move to next node
            current_node = current_node.next
        
    
    def delete_head(self):
        # Removes the head(first node) of the list.
        
        # set the head's next to be the head
        self.head = self.head.next
        self.length -= 1
    
    
    def delete_tail(self):
        # Removes the tail(last node) of the list.
        
        # make an iterator to find the tail and remove it
        current_node = self.head
        for _ in range(self.length):
            # if next is tail, set current next to None
            if current_node.next == self.tail:
                current_node.next = None
                self.tail = current_node
                self.length -= 1
                return
            
            # if not the above, move to next node
            current_node = current_node.next
            
    # Traversal to Print
    def __str__(self):
        # Prints all the nodes' data linked with '->'
        
        # make an iterator
        linked_list = []
        current_node = self.head
        for _ in range(self.length):
            linked_list.append(current_node.data)
            current_node = current_node.next
        
        return ' -> '.join(linked_list)
    
    def __len__(self):
        return self.length
        
        
if __name__ == "__main__":
    l = LinkedList()
    l.append("김상민")
    print(l)
    print(len(l))
    l.append("박건웅")
    print(l)
    print(len(l))
    l.append("손동현")
    print(l)
    print(len(l))
    l.append("이다경")
    print(l)
    print(len(l))
    l.prepend("자알팀:")
    print(l)
    print(len(l))
    l.insert_after("이다경", "유용석")
    print(l)
    print(len(l))
    l.delete("자알팀:")
    print(l)
    print(len(l))
    l.delete("유용석")
    print(l)
    print(len(l))
    l.delete("박건웅")
    print(l)
    print(len(l))
    l.delete_head()
    print(l)
    print(len(l))
    l.delete_tail()
    print(l)
    print(len(l))
    