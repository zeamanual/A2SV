/**
 * @param {number[]} tokens
 * @param {number} power
 * @return {number}
 */
var bagOfTokensScore = function(tokens, power) {
    tokens.sort((a,b)=>a-b)
    let score =0
    let maxScore = score
    let leftPtr = 0
    let rightPtr = tokens.length-1
    while(leftPtr<=rightPtr){
        if(power>=tokens[leftPtr]){
            power-=tokens[leftPtr]
            leftPtr+=1
            score+=1
        }
        else if(score>=1){
            score-=1
            power+=tokens[rightPtr]
            rightPtr-=1
        }else{
            leftPtr+=1
        }
        if(score>maxScore){
            maxScore=score
        }

    }

    return maxScore
};
