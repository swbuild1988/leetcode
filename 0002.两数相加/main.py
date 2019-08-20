# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prenode = ListNode(0)
        lastnode = prenode
        val = 0
        while l1 or l2 or val:
            cur = val
            cur = cur + (l1.val if l1 else 0)
            cur = cur + (l2.val if l2 else 0)
            val = cur // 10
            cur = cur % 10

            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

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
l1 = generateList([9, 2, 3, 4])
l2 = generateList([2, 7])
printList(l1)
printList(l2)
printList(s.addTwoNumbers(l1, l2))
