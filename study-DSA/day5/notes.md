앞으로의 커리큘럼

1. 링크드 리스트 시작한 것 완성하기
- 참고로 싱글 링크드 리스트인데, 더블리는 아래 내용 참고**
2. 프로그래머스의 코딩테스트 고득점 Kit 코테 문제 연습
- 완전탐색
- 이분탐색
- 해시
- 힙(Heap)
- 깊이/너비 우선 탐색(DFS/BFS)
- 그래프
- 탐욕법(Greedy)
- 동적계획법(Dynamic Programming)


# Doubly Linked List
### 1. **Insertion Methods**
   - **`append(value)`**: Adds a new node with the given value to the end of the list.
   - **`prepend(value)`**: Adds a new node with the given value to the beginning of the list.
   - **`insert_after(node, value)`**: Inserts a new node with the given value after a specified node.
   - **`insert_before(node, value)`**: Inserts a new node with the given value before a specified node.

### 2. **Deletion Methods**
   - **`delete(value)`**: Removes the first node with the specified value from the list.
   - **`delete_head()`**: Removes the head (first node) of the list.
   - **`delete_tail()`**: Removes the tail (last node) of the list.
   - **`delete_node(node)`**: Removes a specific node from the list.

### 3. **Traversal Methods**
   - **`find(value)`**: Searches for a node containing the specified value and returns it if found.
   - **`traverse_forward()`**: Iterates over the list from the head to the tail, typically used to print the values or perform some action on each node.
   - **`traverse_backward()`**: Iterates over the list from the tail to the head, useful for certain algorithms or simply to display the list in reverse order.

### 4. **Utility Methods**
   - **`size()`**: Returns the number of nodes in the list.
   - **`is_empty()`**: Checks if the list is empty.
   - **`reverse()`**: Reverses the order of the nodes in the list by swapping the next and previous pointers.
   - **`get_head()`**: Returns the head (first node) of the list.
   - **`get_tail()`**: Returns the tail (last node) of the list.

### 5. **Display Methods**
   - **`__str__()` or `__repr__()`**: Provides a string representation of the list for easy visualization, either forward or backward.

### Optional Methods
   - **`sort()`**: Sorts the elements of the doubly linked list.
   - **`merge(other_list)`**: Merges another doubly linked list into the current list.