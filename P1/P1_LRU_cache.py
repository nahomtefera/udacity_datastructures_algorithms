class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.hash_table = dict({})
        self.capacity = capacity
        self.num_of_entries = 0
        self.usage_order = list()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        for index, element in enumerate(self.usage_order):
          if element == key:
            del self.usage_order[index]
            self.usage_order.insert(0,key)
            break
        if key in self.hash_table:
          print("num of entriees:",self.num_of_entries)
          print("hash table:",self.hash_table)
          print("usage order:",self.usage_order)
          return self.hash_table[key]

        print("entry not found: -1", key)
        print("num of entriees:",self.num_of_entries)
        print("hash table:",self.hash_table)
        print("usage order:",self.usage_order)
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.hash_table:
          return
        elif self.num_of_entries < self.capacity:
          self.hash_table[key] = value
          self.num_of_entries += 1
          self.usage_order.insert(0, key)
        elif self.num_of_entries == self.capacity:
          oldest_item = self.usage_order.pop()
          self.hash_table.pop(oldest_item, None)
          self.hash_table[key] = value
          self.usage_order.insert(0, key)
        print("num of entriees:",self.num_of_entries)
        print("hash table:",self.hash_table)
        print("usage order:",self.usage_order)


print("\n ==> our_cache = LRU_Cache(5)")
our_cache = LRU_Cache(5)
print("\n ==> our_cache.set(1, 1);")
our_cache.set(1, 1);
print("\n ==> our_cache.set(2, 2);")
our_cache.set(2, 2);
print("\n ==> our_cache.set(3, 3);")
our_cache.set(3, 3);
print("\n ==> our_cache.set(4, 4);")
our_cache.set(4, 4);

print("\n ==> our_cache.get(1)")
our_cache.get(1)       # returns 1
print("\n ==> our_cache.get(2)")
our_cache.get(2)       # returns 2
print("\n ==> our_cache.get(9)")
our_cache.get(9)      # returns -1 because 9 is not present in the cache

print("\n ==> our_cache.set(5, 5)")
our_cache.set(5, 5) 
print("\n ==> our_cache.set(6, 6)")
our_cache.set(6, 6)

print("\n ==> our_cache.get(3)")
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

