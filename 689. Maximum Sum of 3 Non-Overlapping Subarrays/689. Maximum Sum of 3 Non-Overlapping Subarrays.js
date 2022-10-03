/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSumOfThreeSubarrays = function(nums, k) {
    let prefixSum = []
    let arraySize = nums.length
    let prevValue = 0
    for (let i = 0;i<arraySize;i++){
        prefixSum[i]=nums[i]+prevValue
        prevValue = prefixSum[i]
    }


    let sums = []
    for(let i = 0;i<arraySize;i++){
        let leftSideSum = i>0?prefixSum[i-1]:0
        let rightSideSum = prefixSum[i+k-1]
        sums[i]=rightSideSum-leftSideSum

        if((i+k-1)>=arraySize-1){
            break
        }
    }


    let leftSide = []
    let maxIndex = 0
    let sumsSize = sums.length
    for(let i = 0;i<sumsSize;i++){
        if(sums[i]>sums[maxIndex]){
            maxIndex=i
        }
        leftSide[i]=maxIndex
    }


    let rightSide = []
    maxIndex=sumsSize-1
    for(let i = sumsSize-1;i>=0;i--){
        if(sums[i]>=sums[maxIndex]){
            maxIndex=i
        }
        rightSide[i]=maxIndex
    }

    let result = []
    let MaxSum = ''
    for (let i = k;i<sumsSize-k;i++){
        let first = i
        let second = leftSide[i-k]
        let third = rightSide[i+k]
        let currentSum = sums[first] + sums[second] + sums[third]
        if((result[0]==undefined) || currentSum>MaxSum ){
             result[0]=second
             result[1]=first
             result[2]= third
             MaxSum=sums[first] + sums[second] + sums[third]
         }
    }

    return result

};
