def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head or not head.next:
        return True

    tmp_list = []
    while head:
        tmp_list.append(head.val)
        head = head.next

    length = len(tmp_list)
    for i in range(0, length / 2):
        if tmp_list[i] != tmp_list[length - i - 1]:
            return False
    return True