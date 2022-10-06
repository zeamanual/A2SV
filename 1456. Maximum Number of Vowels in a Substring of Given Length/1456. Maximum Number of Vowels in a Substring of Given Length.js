/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    let stringSize = s.length
    let leftPtr = 0
    let rightPtr = k-1

    let previousVowelCount = s.slice(leftPtr,rightPtr+1).split('').reduce(
        (accumulator,currentChar)=>{
            if(isVowel(currentChar)){
                return accumulator+1
            }else{
                return accumulator
            }
        },
        0
    )
    let result = previousVowelCount
    
    while(rightPtr<stringSize){
        if(leftPtr>0){
            let tempVowelcount = previousVowelCount -isVowel(s[leftPtr-1])+isVowel(s[rightPtr])
            if(tempVowelcount>result){
                result=tempVowelcount
            }
            previousVowelCount=tempVowelcount
        }
        leftPtr+=1
        rightPtr+=1
    }

    return result
};

let isVowel = (char)=>{
    let vowels = ['a','e','i','o','u']
    if(vowels.includes(char)){
        return 1
    }
    return 0
}
