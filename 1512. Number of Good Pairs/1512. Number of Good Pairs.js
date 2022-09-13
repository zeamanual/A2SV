/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let numberOfGoodPairs= 0
    let length = nums.length
    for(let index in nums){
        let currentIndex = Number(index)
        let tempIndex = currentIndex+1
        while(tempIndex<length){
            if(nums[currentIndex]==nums[tempIndex]){
                numberOfGoodPairs+=1
            }

            tempIndex+=1
        }
    }
    return numberOfGoodPairs
};
