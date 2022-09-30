/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let firstPtr = 0
    let secondPtr = 0
    let max=0
    let stringSize = s.length
    let lastIndex = stringSize-1

    while(secondPtr<=lastIndex){
        let tempSubArray = s.slice(firstPtr,secondPtr)
        if(tempSubArray.includes(s[secondPtr])){
            while(s[firstPtr]!==s[secondPtr]){
                firstPtr+=1
            }
            firstPtr+=1

        }

        let tempMax = secondPtr-firstPtr+1
        if(tempMax>max){
            max=tempMax
        }
        secondPtr+=1
    }
    return max
};
