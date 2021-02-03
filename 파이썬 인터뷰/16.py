from ListNode import ListNode, get_linked_list


num1 = get_linked_list([2, 4, 3])
num2 = get_linked_list([5, 6, 4])


def add_two_number(n1: ListNode, n2: ListNode):
    carry = 0
    root = head = ListNode(0)
    while n1 or n2 or carry:
        s = 0
        if n1:
            s += n1.val
            n1 = n1.next
        if n2:
            s += n2.val
            n2 = n2.next
        carry, val = divmod(s + carry, 10)
        head.next = ListNode(val)
        head = head.next
    return root.next


result = add_two_number(num1, num2)

print(result)
