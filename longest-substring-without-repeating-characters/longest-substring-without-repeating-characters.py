/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let firstPtr=0
    let secondPtr=0
    let longest=s.length>0?1:0
    let detail=new Map()

    while(secondPtr<s.length){
        if(detail.has(s[secondPtr])){
            let tempLongest = secondPtr-firstPtr
            longest=Math.max(longest,tempLongest)
            while(s[firstPtr]!==s[secondPtr]){
                detail.delete(s[firstPtr])
                firstPtr++
            }
            firstPtr++
        }else{
            let tempLongest = secondPtr-firstPtr+1
            longest=Math.max(longest,tempLongest)
        }

        detail.set(s[secondPtr],secondPtr)
        secondPtr++
    }
    return longest
};
