class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.hash_table = dict({})
        self.capacity = capacity
        self.num_of_entries = 0
        self.usage_order = list()

    def get(self, key):
        if key is None:
          return "Can't get null values"
        # Retrieve item from provided key. Return -1 if nonexistent. 
        for index, element in enumerate(self.usage_order):
          # remove item and place it at the beggining of our list
          if element == key:
            del self.usage_order[index]
            self.usage_order.insert(0,key)
            break
          
        if self.hash_table.get(key):
          return self.hash_table[key]

        return -1

    def set(self, key, value):
        if self.capacity < 1:
          return "Capacity of cache should be more than 0"
        if (key is None or not isinstance(key, int)) or value is None:
          return "Can't set null values or non int"
        # Set the value if the key is not present in the cache. 
        if self.hash_table.get(key):
          # If the key is present in the cache, since we are attemting to set it again
          # add it to the beggining of our usage_order
          for index, element in enumerate(self.usage_order):
            # remove item and place it at the beggining of our list
            if element == key:
              del self.usage_order[index]
              self.usage_order.insert(0,key)
              break

        elif self.num_of_entries < self.capacity:
          # if cache is not at capacity, add item
          self.hash_table[key] = value
          self.num_of_entries += 1
          self.usage_order.insert(0, key)
        elif self.num_of_entries == self.capacity:
          # if cache is at capacity, remove oldest item
          # add new item
          oldest_item = self.usage_order.pop()
          self.hash_table.pop(oldest_item, None)
          self.hash_table[key] = value
          self.usage_order.insert(0, key)


our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)     # returns 1
our_cache.get(2)     # returns 2
our_cache.get(9)     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.get(9)     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# ADDITIONAL TEST CASES

cache_test = LRU_Cache(4)
cache_test.set(23, "Testing 23")
cache_test.set(13, "Testing 13")

print(cache_test.get(23))
# returns "Testing 23"
print(cache_test.get(13))
# returns "Testing 13"
print(cache_test.set(None, 1)) 
# edge case returns "Can't set null values or non int"
print(cache_test.set("", 23))
# edge case returns "Can't set null values or non int" 

cache_edge_test = LRU_Cache(-1)
print(cache_edge_test.set(3, "Testing 3"))
# edge case returns "Capacity of cache should be more than 0"

cache_edge_test_2 = LRU_Cache(0)
print(cache_edge_test_2.set(13, "Testing 13"))
# edge case returns "Capacity of cache should be more than 0"

cache_edge_test_3 = LRU_Cache(10000)
cache_edge_test_3.set(3, "Testing 3")
print(cache_edge_test_3.get(3))
# edge case returns testing3