class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):

  def traverse_groups(user, group):
    # recursive method
    users = group.get_users()
    groups = group.get_groups()
    
    if user in users:
      return True

    if len(groups) > 0:
      for g in groups:
        # if current group has nested groups 
        # traverse one by one
        user_found = traverse_groups(user, g)
        if user_found is True:
          return True

    return False
  return traverse_groups(user, group)  


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child.add_user("sub_child_user-2")

child.add_group(sub_child)
parent.add_group(child)


print(is_user_in_group("sub_child_user", parent))

## additional tests
grand_parent = Group("grand parent")
uncle = Group("uncle")
uncle.add_user("bob")
uncle.add_user("rosa")
uncle.add_user("")
cousins = Group("cousins")
cousins.add_user("rocio")
cousins.add_user("marta")
primos = Group("primos")
primos.add_user("jona")
primos.add_user("woini")
uncle.add_group(Group("weird cousins"))
uncle.add_group(Group("weird aunt"))
uncle.add_group(cousins)
parent.add_group(primos)
grand_parent.add_group(parent)
grand_parent.add_group(uncle)


print(is_user_in_group("jona", uncle))
# returns False since "jona" is not in the group "uncle"

print(is_user_in_group("", uncle))
# returns True, there is a user with an empty string in "uncle"

print(is_user_in_group(None, grand_parent))
# returns False, there are no groups with user "None"