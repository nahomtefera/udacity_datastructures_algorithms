
# Problem 4 - P4_Active_Directory

  ## For this problem I'm using a lists to store usrs and groups and I'm using recursion function to traverse through each group.

  ### Time complexity

    - Worst Case Complexity: O(mn) - where m is the number of users and n the number of nested groups. The worst case would be looking up the last user in the deepest nested group. 

  ### Space complexity

    - Worst Case Complexity: O(mn) - since there will be multiple traverse_groups() running simultaneously until we find the user or until every group has been checked.
