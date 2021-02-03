from ListNode import ListNode, get_linked_list, get_list


def odd_even_list(head: ListNode):
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head


root = odd_even_list(get_linked_list([1, 2, 3, 4, 5]))

print(get_list(root))
