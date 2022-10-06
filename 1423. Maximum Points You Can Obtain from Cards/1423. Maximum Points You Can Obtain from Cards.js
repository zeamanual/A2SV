/**
 * @param {number[]} cardPoints
 * @param {number} k
 * @return {number}
 */
var maxScore = function(cardPoints, k) {
    let cardLength = cardPoints.length
    let lastIndex = cardLength-1
    let leftPtr = 0
    let rightPtr = lastIndex-k
    let max=0
  

    for(let i =0;i<k;i++){
        max+=cardPoints[lastIndex-i]
    }
    let result=max
    if(k==cardLength){
        return result
    }
    while(rightPtr<cardLength){
        let leftSide = leftPtr>0?cardPoints[leftPtr-1]:0
        let rightSide = (lastIndex-rightPtr)==k?0:cardPoints[rightPtr]
        max = max+leftSide -rightSide
        if(max>result){
            result=max
        }
        leftPtr+=1
        rightPtr+=1
    }

    return result
};
