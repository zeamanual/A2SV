/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let prefix = []
    let postfix = []
    let prevProduct = 1

    // calculating prefix product
    for ( let number of nums){
        let currentResult = prevProduct*number
        prefix.push(currentResult)
        prevProduct=currentResult
    }

    // calculating postfix product
    let arraySize = nums.length
    prevProduct = 1
    for(let i=arraySize-1;i>-1;i-- ){
        let currentResult = nums[i]*prevProduct
        postfix[i]=currentResult
        prevProduct = currentResult
    }

    let finalResult = []
    for( let i = 0;i<arraySize;i++){
        let prefixValue = i>0?prefix[i-1]:1
        let postFixValue = (i<arraySize-1)?postfix[i+1]:1
        let tempResult = prefixValue*postFixValue
        finalResult.push(tempResult)
    }
    return finalResult
};
