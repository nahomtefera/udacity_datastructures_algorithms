import hashlib
import datetime  

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.next = None
      self.index = 0
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = self.data.encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.previous_hash).encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

    def set_index(self, index):
      self.index = index
    
    def set_next(self, block):
      self.next = block


class BlockChain:
  def __init__(self):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    genesis_block = Block(timestamp, "Genesis Block", 0)
    self.head = genesis_block
    self.tail = genesis_block
    self.order = list([genesis_block])
    self.size = 1
  
  def append(self, data, timestamp=None):
    if data is None:
      return "Not a valid type"
    if timestamp is None:
      timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    new_block = Block(timestamp, data, self.tail.hash)
    new_block.set_index(self.size) 
    self.tail.next = new_block
    self.tail = new_block
    self.order.append(new_block)
    self.size += 1
  

## Test cases

new_block_chain = BlockChain()

new_block_chain.append('paying luke $10')
new_block_chain.append('paying jona $40')
new_block_chain.append('$50 deposited')

block = new_block_chain.head

while block:
  print('index', block.index)
  print('data', block.data)
  print('hash', block.hash)
  print('prev_hash', block.previous_hash)
  block = block.next
  ## it will print index, hash and previous_hash for every block in the chain



print("========TEST CASE 2========")

dripcoin = BlockChain()

print(dripcoin.append(None))

print("========TEST CASE 3========")
# it will return "Not a valid type"
dripcoin.append('give mee the moneeeyz')
dripcoin.append('')

block = dripcoin.head

while block:
  print('index', block.index)
  print('data', block.data)
  print('hash', block.hash)
  print('prev_hash', block.previous_hash)
  block = block.next
  ## it will print index, hash and previous_hash for every block in the chain


print("========TEST CASE 4========")
## adding blocks with the same timestamp
bchain = BlockChain()

bchain.append('car payment - $300')
print(bchain.tail.timestamp)
bchain.append('netflix - $15')
print(bchain.tail.timestamp)
bchain.append('hulu - $11')
print(bchain.tail.timestamp)

block = bchain.head

while block:
  print('index', block.index)
  print('data', block.data)
  print('hash', block.hash)
  print('prev_hash', block.previous_hash)
  block = block.next
  ## it will print index, hash and previous_hash for every block in the chain

