# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        prenode = ListNode(0)
        lastnode = prenode
        while (l1 and l2):
            val = min(l1.val, l2.val)
            lastnode.next = ListNode(val)
            lastnode = lastnode.next
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
        if l1:
            lastnode.next = l1
        if l2:
            lastnode.next = l2

        return prenode.next


def generateList(l):
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l):
    while l:
        print("%d, " % (l.val), end='')
        l = l.next
    print('')


s = Solution()
l1 = generateList([1, 2, 4])
l2 = generateList([1, 3, 4])
printList(s.mergeTwoLists(l1, l2))
