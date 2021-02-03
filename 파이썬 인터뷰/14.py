class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


def merge_two_list(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = merge_two_list(l1.next, l2)
    return l1


head = merge_two_list(list1, list2)
print(head)