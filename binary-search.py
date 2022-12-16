class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def find(self, key) -> str:
        """
        Find node by key and return its value
        """
        if key == self.key:
            return self.value
        if key < self.key:
            if self.left is None:
                return None
            return self.left.find(key)
        if key > self.key:
            if self.right is None:
                return None
            return self.right.find(key)
        return None

    def insert(self, key, value):
        """
        Insert a node in the tree
        This method does not allowed duplicated keys
        """
        if key == self.key:
            print("No duplcated keys allowed!")
            return None
        if key < self.key:
            if self.left is not None:
                return self.left.insert(key, value)
            self.left = Node(key, value)
        if key > self.key:
            if self.right is not None:
                return self.right.insert(key, value)
            self.right = Node(key, value)

    def delete(self, key):
        """
        Remove a node from the tree
        """
        if self == None:
            return self
        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
            return self
        if key > self.key:
            if self.right:
                self.right = self.right.delete(key)
            return self

        if self.right == None:
            return self.left
        if self.left == None:
            return self.right

        successor = self.right
        while successor.left:
            successor = successor.left
        self.key = successor.key
        self.right = self.right.delete(successor.key)
        return self

    def print_sorted(self):
        print(self._get_sorted_list([]))

    def _get_sorted_list(self, values):
        if self.left is not None:
            self.left._get_sorted_list(values)
        if self.value is not None:
            values.append(self.value)
        if self.right is not None:
            self.right._get_sorted_list(values)
        return values


# Watch it working
if __name__ == "__main__":
    # The values are the same as the keys so
    # will be easier to evaluate this code,
    # but value could be anything you want =)
    tree = Node(9, "9")
    tree.insert(4, "4")
    tree.insert(1, "1")
    tree.insert(6, "6")
    tree.insert(5, "5")
    tree.insert(7, "7")
    tree.insert(8, "8")
    tree.insert(3, "3")
    tree.print_sorted()

    # let's delete a few
    tree.delete(5)
    tree.print_sorted()
    tree.delete(1)
    tree.print_sorted()

    # and, of course, let's find some nodes
    print(f"Value for 7 is {tree.find(7)}")
    print(f"Value for 8 is {tree.find(8)}")
    print(f"Value for 84 is {tree.find(84)}")
