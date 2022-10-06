/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function(arr, k, threshold) {
    let leftPtr = 0
    let rightPtr = k-1
    let arraySize = arr.length
    let result=0
    
    let previousSum = arr.slice(leftPtr,rightPtr+1).reduce((accumulator,currentValue)=>{
        return accumulator+currentValue
    },0)
    while(rightPtr<arraySize){
        let removed = leftPtr>0?arr[leftPtr-1]:0
        let added =rightPtr!==k-1? arr[rightPtr]:0
        let tempSum = previousSum-removed+added
        if((tempSum/k)>=threshold){
            result+=1
        }
        previousSum=tempSum
        leftPtr+=1
        rightPtr+=1
    }

    return result
};
