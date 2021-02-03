from ListNode import ListNode, get_linked_list


def swap_pairs(head: ListNode):
    if head and head.next:
        p = head.next
        head.next = swap_pairs(p.next)
        p.next = head
        return p
    return head


root = swap_pairs(get_linked_list([1, 2, 3, 4]))

print(root)