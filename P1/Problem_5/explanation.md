# Problem 5 - P5_Blockchain

  ## For this problem I'm using a linked list that has head and tail

  ### Time complexity

    - Creating a block
      - Worst Case Complexity: the time it takes sha.update to run the hash function. I believe it's O(n) 

    - Appending a block to our BlockChain linked list:
      - Since we set up the linked list so that it will create a new block time complexity will be O(n).
      - The linked list has a tail, that way we can get the prev_hash in O(1).

  ### Space complexity

    - Worst Case Complexity: O(n) - the size of the linked list