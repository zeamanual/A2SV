/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let maxArea = 0
    let leftPtr = 0
    let rightPtr = height.length -1
    
    while(leftPtr<rightPtr){
       let tempMaxArea= (Math.min(height[leftPtr],height[rightPtr])) *(rightPtr-leftPtr)
        if(tempMaxArea>maxArea){
            maxArea = tempMaxArea
        }
        
        if(height[leftPtr]<height[rightPtr]){
            leftPtr+=1
        }else{
            rightPtr-=1
        }
    }
    
    return maxArea
    
};
