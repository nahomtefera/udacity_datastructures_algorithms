# Problem 1 - Square_Root_of_Integer

  ## For this problem I used a binary search algorithm to find the square root of our target. At each step we discard half of the values we are searching through, making the efficiency of the algorith O(log(n)).
  
  ### Time complexity
    - I'm using 2 while loops that discard half of the values in each iteration. Making the algorith O(log(n))

  ### Space complexity
    - Our space complexity is O(1) since our algorith is iterative and the function is only called once, it's running in a single stack frame. We are also allocating a constant number of variables making the space complexity O(1).
