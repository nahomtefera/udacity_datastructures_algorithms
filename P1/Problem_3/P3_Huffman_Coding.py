import sys

# node class
class HuffmanNode:
  def __init__(self, character=None, frequency=None, bit=None):
      self.left_child = None
      self.right_child = None
      self.character = character
      self.frequency = frequency
      self.bit = bit
  #node methods
  def has_left_child(self):
    return self.left_child is not None
  def has_right_child(self):
    return self.right_child is not None
  def get_left_child(self):
    return self.left_child
  def get_right_child(self):
    return self.right_child
  def set_left_child(self, node):
    self.left_child = node
  def set_right_child(self, node):
    self.right_child = node
  def set_bit(self, bit):
    self.bit = bit

# ENCODIING METHOD
def huffman_encoding(data):
  # create a dict to store characters and frequencies
  charTable = dict({})
  for char in data:
    if char not in charTable:
      charTable[char] = 1
    else:
      charTable[char] +=1
  # BUILD HUFFMAN TREEE
  priority_list = buildHuffmanTree(charTable)
  # HUFFMAN TREEE ROOT is the remaining node in the priority list
  huffmanTreeRoot = priority_list.storage[0]

  # to get the huffman code for each character we will traverse DFS our tree
  # the encoder will return a dictionary of characters and codes
  code_hash = encoder(huffmanTreeRoot)
  encoded_data = ""
  # loop through our dictionary of codes to encode the data
  for key in code_hash:
    i = 0
    while i < code_hash[key]["frequency"]:
      encoded_data += code_hash[key]['code']
      i += 1
  
  return encoded_data, huffmanTreeRoot

# DECODING METHOD
def huffman_decoding(data,tree):
  decoded_msg = ''

  i=0
  node = tree
  # loop coded data
  # traverse tree following left or right child depening on current bit (0-left, 1-right)
  while i < len(data):
    bit = data[i]
    if bit == "0":
      node = node.left_child
    if bit == "1":
      node = node.right_child
    # if character value is not 'Internal Node' we found a character in the original data
    if node.character != 'Internal Node':
      decoded_msg += node.character
      # once we decode a prefix, start traversing the tree from the root
      node = tree
    i += 1
  
  return decoded_msg

# HELPER METHODS
# Min Heap
class MinHeap:
  def __init__(self, capacity):
    self.storage = [0] * capacity
    self.capacity = capacity
    self.size = 0
  # Heapify up - used when inserting a node
  def heapify_up(self, index):
    if self.has_parent(index) and self.parent(index).frequency > self.storage[index].frequency:
        self.swap(self.get_parent_index(index), index)
        self.heapify_up(self.get_parent_index(index))
  # Heapify down - used when popping a node
  def heapify_down(self, index):
    smallest_index = index
    if self.has_left_child(index) and self.storage[smallest_index].frequency > self.left_child(index).frequency:
      smallest_index = self.get_left_child_index(index)
    if self.has_right_child(index) and self.storage[smallest_index].frequency > self.right_child(index).frequency:
      smallest_index = self.get_right_child_index(index)
    if smallest_index != index:
      self.swap(index, smallest_index)
      self.heapify_down(smallest_index)
  # insert methodd
  def insert(self, data):
    if self.isFull():
      print("Heap is Full")
    self.storage[self.size] = data
    self.size += 1
    self.heapify_up(self.size - 1)
  # reemove min method
  def remove_min(self):
    if self.size == 0:
      raise('Empty Heap')
    data = self.storage[0]
    self.storage[0] = self.storage[self.size -1]
    self.storage[self.size -1] = 0
    self.size -= 1
    self.heapify_down(0)
    return data
  # node methods
  def get_parent_index(self, index):
    return (index - 1) / 2
  def get_left_child_index(self, index):
    return 2 * index + 1
  def get_right_child_index(self, index):
    return 2 * index + 2
  def has_parent(self, index):
    return self.get_parent_index(index) >= 0
  def has_left_child(self, index):
    return self.get_left_child_index(index) < self.size
  def has_right_child(self, index):
    return self.get_right_child_index(index) < self.size
  def parent(self, index):
    return self.storage[self.get_parent_index(index)]
  def left_child(self, index):
    return self.storage[self.get_left_child_index(index)]
  def right_child(self, index):
    return self.storage[self.get_right_child_index(index)]
  def isFull(self):
    return self.size == self.capacity
  def swap(self, index1, index2):
    temp = self.storage[index1]
    self.storage[index1] = self.storage[index2] 
    self.storage[index2] = temp 
    
# huffman tree method
def buildHuffmanTree(charTable):
  # create a priority list using the min heap function
  # inizialize minheap with a capacity of len(charTable)
  priority_list = MinHeap(len(charTable))

  # loop through our dictionary of characters and frequencies and insert them in the priority list
  for char in charTable:
    # create a node that holds the character and frequency
    # insert the node to our priority list
    frequency = charTable[char]
    node = HuffmanNode(char, frequency)
    priority_list.insert(node)
  
  # once our priority list is set up
  # pop the min 2 nodes 
  # create a new node with the sum of the frequencies
  # set the popped nodes as left_child < right_child of the new nodee
  while priority_list.size > 1:
    # pop 2 min nodes
    node1 = priority_list.remove_min()
    node2 = priority_list.remove_min()
    # create new node with sum of frequencies
    internalNode = HuffmanNode('Internal Node', node1.frequency + node2.frequency)
    # check which frequency is smaller and set left and right child
    if node1.frequency < node2.frequency:
      node1.set_bit(str(0))
      node2.set_bit(str(1))
      internalNode.set_left_child(node1)
      internalNode.set_right_child(node2)
    else:
      node1.set_bit(str(1))
      node2.set_bit(str(0))
      internalNode.set_left_child(node2)
      internalNode.set_right_child(node1)
    # push new node to priority list
    priority_list.insert(internalNode)

  return priority_list
# encoder method
def encoder(root):
  code = list()
  code_hash = dict({})
  def traverse(node):
    # if node is not none we will traverse left and right
    if node:
      # append current node's bit to our code list
      if node.bit is not None:
        code.append(node.bit)
        # if the current node doent' have lef or right children, we found a leaf (character we want to encode)
        if node.left_child == None and node.right_child == None:
          code_hash[node.character] = {"frequency": node.frequency, "code": "".join(code)}
          code.pop()
          return
        # visit_order.append([node.frequency, node.character, node.bit])
      traverse(node.left_child)
      traverse(node.right_child)
      # once left and right traversal has been done, remove bit from code to build next branch
      if len(code) > 0:
        code.pop()

  traverse(root)
  return code_hash



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
