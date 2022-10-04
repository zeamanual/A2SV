/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    if(lists.length==1){
        return lists[0]
    }else if(lists.length<1){
        return null
}
    let middle = Math.floor(lists.length/2)
    let arraySize = lists.length
    let leftSorted = mergeKLists(lists.slice(0,middle))
    let rightSorted = mergeKLists(lists.slice(middle,arraySize))
    let merged = merge(leftSorted,rightSorted)

    return merged

};

let merge = (listOne,listTwo)=>{

    let ptrOne= listOne
    let ptrTwo = listTwo
    let dummyNode = new ListNode()
    let tail = dummyNode;


    while(ptrOne !==null && ptrTwo !==null){
        if(ptrOne.val<ptrTwo.val){
            tail.next=ptrOne
            ptrOne=ptrOne.next
        }else {
            tail.next = ptrTwo
            ptrTwo=ptrTwo.next
        }
        tail=tail.next
    }
    
    while(ptrOne!==null){
        tail.next=ptrOne
        tail=tail.next
        ptrOne= ptrOne.next
    }

    while(ptrTwo!==null){
        tail.next = ptrTwo
        tail= tail.next
        ptrTwo=ptrTwo.next
    }

    return dummyNode.next

}
