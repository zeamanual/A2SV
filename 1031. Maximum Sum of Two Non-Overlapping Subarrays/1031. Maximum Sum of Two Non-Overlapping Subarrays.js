/**
 * @param {number[]} nums
 * @param {number} firstLen
 * @param {number} secondLen
 * @return {number}
 */
var maxSumTwoNoOverlap = function(nums, firstLen, secondLen) {
    // caculating prefixsum of array
    let prefixSum = new Array(nums.length)
    let sum=0
    for(let index=0;index<nums.length;index++){
        sum+=nums[index]
        prefixSum[index]=sum
    }
    let firstMax=getMaxSum(prefixSum,firstLen,secondLen)
    let secondMax=getMaxSum(prefixSum,secondLen,firstLen)
    return Math.max(firstMax,secondMax)
};

let  getMaxSum= (prefixSum,firstLen,secondLen)=>{
    let maxLeftSideSum = Number.NEGATIVE_INFINITY
    let maxSum = Number.NEGATIVE_INFINITY
    for(let index =0;index<=prefixSum.length-firstLen-secondLen;index++){
        let leftSideRedcueBy = index>0?prefixSum[index-1]:0
        let currentLeftSideSum = prefixSum[(firstLen-1)+index]-leftSideRedcueBy
        let rightSideReduceBy = prefixSum[(firstLen-1)+index]
        let currentRightSideSum = prefixSum[(firstLen+secondLen-1)+index]-rightSideReduceBy
        maxLeftSideSum=Math.max(currentLeftSideSum,maxLeftSideSum)
        maxSum=Math.max(maxSum,maxLeftSideSum+currentRightSideSum)
    }

    return maxSum
}

