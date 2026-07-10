class ListNode:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self):
        self.head = self.tail = ListNode(-1)
    
    def get(self, index: int) -> int:
        curr = self.head.next
        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next
        return curr.val if curr else -1
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val,self.head.next)
        self.head.next = new_node
        if self.tail == self.head:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        for _ in range(index):
            curr = curr.next
            if not curr or not curr.next:
                return False
        if curr.next:
            curr.next = curr.next.next
            if not curr.next:
                self.tail = curr
            return True
        return False

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.next
        while curr != None:
            vals.append(curr.val)
            curr = curr.next
        return vals
        