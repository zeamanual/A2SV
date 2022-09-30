/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let prefixSum = []
    if(nums.length<1){
        return -1
    }
    prefixSum[0]=nums[0]
    let arraySize = nums.length
    for(let i = 1;i<arraySize;i++){
        prefixSum[i]=prefixSum[i-1]+nums[i]
    }
    for (let index = 0;index<arraySize;index++){
        let rightSideSum = prefixSum[arraySize-1]-prefixSum[index]
        let leftSideSum = index>0?prefixSum[index-1]:0
        if(leftSideSum===rightSideSum){
            return index
        }
        continue
    }

    return -1
};
