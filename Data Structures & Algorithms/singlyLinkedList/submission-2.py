class ListNode:
    def __init__(self,val,next=None):
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
        if self.head == self.tail:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        curr = self.head
        for _ in range(index):
            if not curr.next:
                return False
            curr = curr.next
        if curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        vals = []
        while curr != None:
            vals.append(curr.val)
            curr = curr.next
        return vals
