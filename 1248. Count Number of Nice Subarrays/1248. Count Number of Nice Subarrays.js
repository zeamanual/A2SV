/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numberOfSubarrays = function(nums, k) {
    let arraySize = nums.length
    for (let index= 0;index<arraySize;index++){
        if(nums[index]%2==0){
            nums[index]=0
        }else{
            nums[index]=1
        }
    }

    let keyValuePair = {
        0:1
    }
    
    let sum = 0
    let count = 0
    for (let num of nums){
        sum+=num
        let tempDiff = sum-k

        if(keyValuePair[tempDiff]!==undefined){
            count+=keyValuePair[tempDiff]
        }

        if(keyValuePair[sum]!==undefined){
            keyValuePair[sum]+=1
        }else{
            keyValuePair[sum]=1
        }
    }

    return count
};
