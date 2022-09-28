/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    
    let firstPtr = head
    let tempPrev = null
    let temp = head
    for( let i = 0;i<n;i++){
        temp = temp.next
    }
    
    let secondPtr = temp
    while(secondPtr!==null){
        tempPrev = firstPtr
        firstPtr = firstPtr.next
        secondPtr = secondPtr.next
    }
    
    if(tempPrev !==null){
        tempPrev.next = firstPtr.next
    }else{
        head = firstPtr.next
    }
    return head
};
