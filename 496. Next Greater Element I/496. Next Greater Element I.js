/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    let stack = []
    let result = {}

    for (let currentNum of nums2){
        if(stack.length==0 || stack[stack.length-1]>=currentNum){
            stack.push(currentNum)
        }else{
            let lastElement = stack[stack.length-1]
            while(lastElement<currentNum){
                result[lastElement]=currentNum
                stack.pop()
                lastElement=stack[stack.length-1]
            }
            stack.push(currentNum)
        }
    }

    let finalResult = []
    for (let number of nums1){
        if(result[`${number}`]!==undefined){
            finalResult.push(result[`${number}`])
        }else{
            finalResult.push(-1)
        }
    }

    return finalResult
};
