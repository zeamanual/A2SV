/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    let dummyNode =new ListNode(0,head)
     
    let firstPtr = dummyNode
    let secondPtr = head
    
    while( (secondPtr !== null) &&  secondPtr.next!==null){
        if(secondPtr.val == secondPtr.next.val){
            while( (secondPtr.next !== null) && ( secondPtr.val ==secondPtr.next.val)){
                secondPtr = secondPtr.next
            }
            firstPtr.next=secondPtr.next
            secondPtr=secondPtr.next
        }else{
            firstPtr=firstPtr.next
            secondPtr = secondPtr.next
        }
    }
    
    return dummyNode.next
};
