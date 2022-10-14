/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    let stack = []
    let result = []
    
    for(let index = 0;index<temperatures.length;index++){
        if(stack.length>0){
            let lastTempIndex = stack[stack.length-1]
            while(temperatures[lastTempIndex]<temperatures[index]){
                result[lastTempIndex]=index-lastTempIndex
                stack.pop()
                lastTempIndex = stack[stack.length-1]
            }

        }
        stack.push(index)
    }
    for(let leftTempIndex of stack){
        result[leftTempIndex]=0
    }
    return result
};
