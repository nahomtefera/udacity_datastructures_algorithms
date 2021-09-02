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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child.add_user("sub_child_user-2")

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
  """
  Return True if user is in the group, False otherwise.

  Args:
    user(str): user name/id
    group(class:Group): group to check user membership against
  """
  def traverse_group(user, group):
    users = group.get_users()
    groups = group.get_groups()

    if len(users) > 0:
      return user in users 

    elif len(groups) > 0:
      for g in groups:
        return traverse_group(user, g)
  return traverse_group(user, group)

print(is_user_in_group("sub_child_user", parent))