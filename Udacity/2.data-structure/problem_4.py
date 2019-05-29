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
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if not user or not group: raise Exception("user or group cannot be empty")
    if not isinstance(group, Group): raise TypeError("group should be Group type")
    if not isinstance(user, str): raise TypeError("user should be string")

    if user in group.get_users(): return True
    
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group): return True
    
    return False

print("=== test case 1 ===")
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)
print(is_user_in_group(sub_child_user, parent))
# should return True

print("=== test case 2 ===")
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
print(is_user_in_group(sub_child_user, parent))
# should return False

print("=== test case 3 ===")
print(is_user_in_group("", parent))
# should output an exception: user or group cannot be empty

print("=== test case 4 ===")
print(is_user_in_group(sub_child_user, "parent"))
# should output an exception: group should be Group type