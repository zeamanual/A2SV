/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    let numberOfBoats = 0
    let leftPtr = 0
    let rightPrt = people.length-1
    people.sort((a,b)=>a-b)

    while(leftPtr<=rightPrt){
        if(people[leftPtr]+people[rightPrt]<=limit){
            leftPtr+=1
            rightPrt-=1
        }else{
            rightPrt-=1
        }

        numberOfBoats+=1
    }

    return numberOfBoats
};
