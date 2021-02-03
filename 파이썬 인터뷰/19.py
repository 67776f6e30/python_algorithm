from ListNode import ListNode, get_linked_list, get_list


def reverse_between(head: ListNode, m: int, n: int):
    root = start = ListNode(None)
    root.next = head
    for _ in range(m - 1):
        start = start.next
    end = start.next
    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return head


data = get_linked_list([1, 2, 3, 4, 5])
print(get_list(reverse_between(data, 2, 4)))
