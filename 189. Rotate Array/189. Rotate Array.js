/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    let numCopy=[...nums]
    let total = nums.length
    for(let i = 0;i<total;i++){
        let finalIndex = getIndex(i,k,total)
        nums[finalIndex]=numCopy[i]
    }

    return nums
};
let getIndex = (currentIndex,shift,total)=>{
    shift=shift%total
    let result = currentIndex+shift
    if(result<=total-1){
        return result
    }else{
        return result-total
    }
}
