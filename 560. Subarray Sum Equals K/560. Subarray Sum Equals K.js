/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {

    let count =0
    let sum = 0
    let keyValuePair = {
        0:1
    }

    for(let num of nums){
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
    console.log(keyValuePair)
    return count
};
