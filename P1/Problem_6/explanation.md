# Problem 6 - P6_Union_And_Intersection

  ## For the union method I'm creating a new linked list and appending each node, for the intersection method I'm using a dictionary to keep track of nodes that are in both lists.

  ### Time complexity

    - Union Worst Case Complexity: O(m*n)
      - We are looping through both Linked Lists and adding them to a new LL. the append method in the Linked List runs in O(n) since we have to traverse the lits every time we append a new node.

    - Intersection Wors Worst Case Complexity: O(mn)
      - Lopping through each list takes O(n), dict operations take O(1), appending to LL takes O(n)

  ### Space complexity

    - Union Worst Case Complexity: O(m) - the size of the linked we return list will be the sum of both linked lists

    - Intersection Worst Case Complexity: O(n) - when lists are identical