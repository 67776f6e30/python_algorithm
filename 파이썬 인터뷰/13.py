class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


data = ListNode(1)
dh = data
data.next = ListNode(2)
data = data.next
data.next = ListNode(3)
data = data.next
data.next = ListNode(2)
data = data.next
data.next = ListNode(1)


def is_palindrome(head: ListNode):
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


print(is_palindrome(dh))
