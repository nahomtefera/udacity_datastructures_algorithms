# Problem 3 - P3_Huffman_Coding

  ## For this problem I used a dictionary to keep track of the frequency of each character to perform operations in O(1), a priority list, and a tree to encode the data.
  
  ### Time complexity
    - huffman_encoding() has a time complexity of O(n log n)
      - loop data, add to dict: O(n)
      - buildHuffmanTree(): O(n log n)
        - loop through dict: O(n)
          - inserting to priority list, min heap: O(log n)
        - building tree: O(n)
      - encoder(): DFS traversal: O(n)
      - loop to create encoded string: O(n)

    - huffman_decoding() has a time complexity of O(n log n)
      - loop data: O(n)
      - traverse tree: O(log n)

  ### Space complexity
    - Both huffman_encoding() and huffman_decoding() methods have a space complexity of O(n). 