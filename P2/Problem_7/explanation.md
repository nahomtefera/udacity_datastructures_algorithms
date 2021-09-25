# Problem 7 - Request Routing in a Web Server with a Trie

  ## For this problem I drilled down the methods for routes and handlers on multiple levels, from the Router to the RouteTrie to the TrieNode and used simple for loops to stablish a decision tree to insert the routes in the trie.
  
  ### Time complexity
    - The time complexity to insert() and lookup() routes in the trie is O(n) depending on the depth of the route. Since search and insertion on a dictionary is O(1) the time complexy will be determined by how deep down the dictionary is our path.

  ### Space complexity
    - The space complexity to insert() and lookup() routes is O(n) since the space we are allocating to hold the routes increases as the input grows.