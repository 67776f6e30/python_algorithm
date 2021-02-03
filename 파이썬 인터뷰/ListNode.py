from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_linked_list(arr: List):
    if not len(arr):
        return None
    head = node = ListNode(arr[0])
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    return head


def get_list(node: ListNode):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr
