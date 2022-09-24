/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function(s) {
    let stack = []
    for(let char of s){
        if(char ==')'){
            temp = []
            let ch = stack.pop()
            while(ch !=='('){
                temp.push(ch)
                ch=stack.pop()
            }
            stack.push(...temp)
        }else{
            stack.push(char)
        }
        
    }
    return stack.join('')
};
