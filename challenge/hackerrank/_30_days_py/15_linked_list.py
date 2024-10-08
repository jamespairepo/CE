class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # For each node except the first node
        if type(head) == Node:
            new_node = head

            while new_node.next:
                new_node = new_node.next

            new_node.next = Node(data)

        #First node
        else:
            head = Node(data)
        return head

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)


# Sample Input
# 4
# 2
# 3
# 4
# 1

# Sample Output
# 2 3 4 1