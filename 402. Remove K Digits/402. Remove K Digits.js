/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function (num, k) {
    let stack = []
    let removed = 0
    let charIdex = 0
    while (charIdex < num.length) {
        while(stack[stack.length-1]>num[charIdex] && removed<k ){
            stack.pop()
            removed+=1
        }
        stack.push(num[charIdex])
        charIdex+=1
    }
    while(removed<k){
        stack.pop()
        removed+=1
    }

    let startIndex = 0
    while(stack[startIndex]=='0'){
        startIndex+=1
    }
    let finalResult=stack.slice(startIndex).join('')
    return finalResult.length>0?finalResult:'0'
};
