/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let arraySize = nums.length
    let leftPtr = 0
    let rightPtr = 0
    let max = 0
    let flipCount = 0
    
    while(rightPtr<=arraySize-1){
        if(nums[rightPtr] ==1){
            rightPtr+=1
        }else if((nums[rightPtr] == 0) && (flipCount<k)){
            rightPtr+=1
            flipCount+=1
        }else{
         
            if(nums[leftPtr]==0){
                flipCount-=1
            }
            leftPtr+=1
        }

        let tempWindowSize = rightPtr-leftPtr
        if(tempWindowSize>max){
            max=tempWindowSize
        }
    }

    return max
};
