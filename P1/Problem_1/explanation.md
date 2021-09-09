# Problem 1 - P1_LRU_cache

  ## For this problem I chose to use a dictionary to lookup key value pairs in our cache in constant time. I also used a list to easily rearange the usage order of the elements added to the cache and pop/append elements.
  
  ### Time complexity
    - get() method runs in O(1) time. 
        - We have a for loop that in the worst case will run 5 times. 
        - Insert opertion in the list also has O(1) time complexity.
        - Dictionary lookup is O(1)
    - set() method also runs in O(1) time.
        - For loop: O(5) => O(1)
        - Dictionaryy operations: O(1)
        - List operations: O(5) => O(1)

  ### Space complexity
    - Both get() and set() methods have a space complexity of O(capacity) => O(1) since the loops within them run against a constant.
