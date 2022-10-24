/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
    let lastOccurences = new Map()
    let finalResult = []

    for(let i = 0;i<s.length;i++){
        lastOccurences.set(s[i],i)
    }

    let leftPrt=0
    let rightPtr = 0
    for(let i = 0;i<s.length;i++){
        rightPtr=Math.max(lastOccurences.get(s[i]),rightPtr)
        if(i==rightPtr){
            finalResult.push(rightPtr-leftPrt+1)
            leftPrt=rightPtr+1
        }
    }

    return finalResult
};
