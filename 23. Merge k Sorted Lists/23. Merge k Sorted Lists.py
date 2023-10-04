# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 1:
            return lists[0]
        elif len(lists) < 1:
            return None

        left_sorted = self.mergeKLists(lists[:len(lists) // 2])
        right_sorted = self.mergeKLists(lists[len(lists) // 2: len(lists)])
        merged = self.merge(left_sorted, right_sorted)

        return merged

    def merge(self,list_one, list_two):

        ptr_one = list_one
        ptr_two = list_two
        dummy_node = ListNode()
        tail = dummy_node

        while ptr_one is not None and ptr_two is not None:
            if ptr_one.val < ptr_two.val:
                tail.next = ptr_one
                ptr_one = ptr_one.next
            else:
                tail.next = ptr_two
                ptr_two = ptr_two.next
            tail = tail.next

        if(ptr_one):
            tail.next=ptr_one
        elif(ptr_two):
            tail.next=ptr_two

        return dummy_node.next
