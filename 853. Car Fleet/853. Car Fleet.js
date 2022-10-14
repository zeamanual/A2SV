/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    let carsData = Array.from(position,(pos,index)=>[pos,speed[index]])
    carsData.sort((a,b)=>a[0]-b[0])
    let totalCars = carsData.length
    let stack = []

    for(let index = totalCars-1;index>=0;index--){
        let currentCarTime = (target-carsData[index][0])/carsData[index][1]
        if(stack.length>0){
            if(stack[stack.length-1]<currentCarTime){
                stack.push(currentCarTime)
            }
        }else{
            stack.push(currentCarTime)
        }
    }

    return stack.length
};
