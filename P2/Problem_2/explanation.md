# Problem 2 - Search_Rotated_Sorted_Array

  ## I approached this problem by finding the location of the pivot first, and then using that information to decide where to look for our target.
  
  ### Time complexity
    - Finding pivot takes O(log(n)) time since we are using a binary search algorithm to lookup values while discarding half of the elemnts in every step.

    - Once we found the pivot in the array the efficiency of finding our target is O(log(n-p)) since we will be discarding a chunk of the array depending on our pivot location and our target.

    - Overall time complexity will be O(log(n)) + O(log(n)) => O(log(n))

  ### Space complexity
    - Similar to the previous problem, our space complexity is O(1) since our call stack is constant as the size of our input grows and we are also allocating a constant number of variables.
    - Space complexity O(1).
