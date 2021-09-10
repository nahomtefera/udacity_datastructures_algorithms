class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
          out_string += str(cur_head.value) + " -> "
          cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
          self.head = Node(value)
          return

        node = self.head
        while node.next:
          node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here    
    united_ll = LinkedList()
    node = llist_1.head
    
    # loop through both lists and append each node to a new node
    while node:
      united_ll.append(node)
      node = node.next

    node = llist_2.head

    while node:
      united_ll.append(node)
      node = node.next

    return united_ll

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersect_ll = LinkedList()
    intersect_dict = dict()

    # add node values from list 1 to dicttionary
    node = llist_1.head
    while node:
      intersect_dict[str(node.value)] = 1
      node = node.next

    node = llist_2.head

    # check if node value iss in dictionary
    # add it to new list if there is a match
    while node:
      if str(node.value) in intersect_dict:
        if intersect_dict[str(node.value)] == 1:
          intersect_ll.append(node)
          intersect_dict[str(node.value)] += 1
      node = node.next

    if intersect_ll.size() > 0:
      return intersect_ll
    return 'No intersection'

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# returns new list with both ll1 and ll2
print (intersection(linked_list_1,linked_list_2))
# returns new list with intersection of ll1 and ll2 = 6 -> 4 -> 21 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# returns new list with both ll1 and ll2
print (intersection(linked_list_3,linked_list_4))
# returns no intersection


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
# returns new list with both ll1 and ll2
print (intersection(linked_list_5,linked_list_6))
# returns no intersection

# Test case 4

linked_list_7 = LinkedList()
# returns new list with both ll1 and ll2
linked_list_8 = LinkedList()
# returns no intersection

element_1 = []
element_2 = [6,7,0,9]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
# returns new list with both ll1 and ll2
print (intersection(linked_list_7,linked_list_8))
# returns no intersection

# Test case 5

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print (union(linked_list_9,linked_list_10))
# returns empty string
print (intersection(linked_list_9,linked_list_10))
# returns no intersection
