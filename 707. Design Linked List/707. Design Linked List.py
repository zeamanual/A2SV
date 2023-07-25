class Node:
    def __init__(self, value = 0, next= None):
        self.value = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size=0
        
    def get(self, index: int) -> int:
        if(index>=self.size):
            return -1
        curr=self.head.next
        count=0
        while(count!=index):
            curr=curr.next
            count+=1
        return curr.value
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next=self.head.next
        self.head.next=new_node    
        self.size+=1

    def addAtTail(self, val: int) -> None:

        curr=self.head
        while(curr.next!=None):
            curr=curr.next
        curr.next=Node(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:

        if(index>self.size):
            return -1
        curr = self.head.next
        prev=self.head
        for i in range(index):
            prev=curr
            curr=curr.next
        to_be_added=Node(val)
        to_be_added.next=curr
        prev.next=to_be_added
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if(index>=self.size):
            return -1
        
        if(index==0):
            self.head.next = self.head.next.next
            self.size-=1
            return

        curr=self.head.next
        for i in range(index-1):
            curr=curr.next
        curr.next=curr.next.next
        self.size-=1
        
    def printfun(self):
        curr = self.head.next
        while curr:
            print(curr.value, end=" ")
            curr = curr.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
