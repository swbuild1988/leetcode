# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        r = []
        for l in lists:
            while l:
                r.append(l.val)
                l = l.next
        r.sort()

        prenode = ListNode(0)
        lastnode = prenode
        for k in r:
            lastnode.next = ListNode(k)
            lastnode = lastnode.next
        
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
l1 = generateList([])
l2 = generateList([1])
# l3 = generateList([1])
printList(s.mergeKLists([l1, l2]))
