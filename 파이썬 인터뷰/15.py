from ListNode import ListNode, get_linked_list


def reverse_list(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next_node, node.next = node.next, prev
        return reverse(next_node, node)
    return reverse(head)


data = get_linked_list([1, 2, 3, 4, 5])

head = reverse_list(data)

print(head)
