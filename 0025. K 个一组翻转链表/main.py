# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        index = 0
        while cur and index < k:
            index += 1
            cur = cur.next

        if index == k:
            cur = self.reverseKGroup(cur, k)
            while index:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                index -= 1
            head = cur
        return head


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
l1 = generateList([1,2,3,4,5,6,7,8])
printList(s.reverseKGroup(l1, 3))
