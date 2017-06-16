"""
You’re given the pointer to the head node of a linked list, an integer to add to
the list and the position at which the integer must be inserted. Create a new
node with the given integer, insert this node at the desired position and return
the head node. A position of 0 indicates head, a position of 1 indicates one
node away from the head and so on. The head pointer given may be null meaning
that the initial list is empty.

Input Format
You have to complete the Node* Insert(Node* head, int data, int position) method
which takes three arguments - the head of the linked list, the integer to insert
and the position at which the integer must be inserted. You should NOT read any
input from stdin/console. position will always be between 0 and the number of
the elements in the list (inclusive).

Output Format
Insert the new node at the desired position and return the head of the updated
linked list. Do NOT print anything to stdout/console.

"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def InsertNth(head, data, position):
    if position == 0:
        new_head = Node(data, head)
        return new_head
    else:
        index = 1
        curr = head
        while index < position:
            curr = curr.next
            index += 1
        next = curr.next
        curr.next = Node(data, next)
    return head
