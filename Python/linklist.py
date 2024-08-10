class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        new_node = SLNode(val)
        if self.head is None:
            self.head = new_node
            return self

        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = new_node
        return self


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

    def print_values(self):
        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next
        return self


my_list = SList()
my_list.add_to_front("are").add_to_front("linked lists").add_to_back("fun!").print_values()
