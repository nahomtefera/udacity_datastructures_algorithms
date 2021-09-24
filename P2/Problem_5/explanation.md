# Problem 5 - Autocomplete with Tries

  ## For the insert() and find() functions I'm using a for loop to traverse through the trie. For the suffixes() method I call the function recursively to find all possible words.
  
  ### Time complexity
    - Insert() and Find() have a time complexity of O(n) given by the lenght of the word we input.

    - Suffixes() has a time complexity of O(n*m) where n is the length or the trie and m the depth for each node.

  ### Space complexity
    - Insert() and Find() have a space complexity of O(1) since we are running the functions in a single stack frame and we have a utilize number of variables.

    - Suffixes() has a space complexity of O(n*m) proportional to the maximum depth generated in our recursive call.