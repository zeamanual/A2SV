/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {

    if(nums.length<=1){
        return nums
    }
    let arraySize = nums.length
    let ptrOne = 0
    let ptrTwo= arraySize-1

    while(ptrOne<ptrTwo){
        if(nums[ptrOne]==0){
            let tempIndex=ptrOne
            while(tempIndex<ptrTwo){
                let tempNumber = nums[tempIndex]
                nums[tempIndex]=nums[tempIndex+1]
                nums[tempIndex+1]=tempNumber
                tempIndex=tempIndex+1
            }
            ptrTwo-=1
        }else{
            ptrOne+=1
        }
    
    }
    
    return nums
};
