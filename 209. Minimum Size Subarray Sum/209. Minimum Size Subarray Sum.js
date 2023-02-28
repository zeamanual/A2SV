/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let minLength =Number.POSITIVE_INFINITY
    let subArrayFound = false

    let prefixSum = []
    let sum =0
    for(let index = 0;index<nums.length;index++){
        sum+=nums[index]
        prefixSum[index]=sum
    }

    let windowStart=0
    let windowEnd = 0

    while(windowEnd<nums.length){
        reduceBy = windowStart>0?prefixSum[windowStart-1]:0
        let currentSum = prefixSum[windowEnd]-reduceBy
        // console.log(currentSum,windowStart,windowEnd)
        if(currentSum>=target){
            subArrayFound=subArrayFound?subArrayFound:!subArrayFound
            minLength=Math.min(minLength,windowEnd-windowStart+1)
            windowStart++
        }else if(currentSum<target){
            windowEnd++
        }
    }

    return subArrayFound?minLength:0
};
