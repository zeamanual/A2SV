/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    let operators = ['+', '-', '/', '*']
    let stack =[]
    let result =tokens[0]
    for(let token of tokens){
        if(operators.includes(token)){
            
            let firstNumber = parseInt(stack.pop())
            let secondNumber = parseInt(stack.pop())
 
            if(token=='+'){
                result = secondNumber + firstNumber
            }else if(token=='-'){
                result = secondNumber - firstNumber                
            }else if(token=='*'){
                result = secondNumber * firstNumber                
            }else{
                result = secondNumber / firstNumber 
                if(result>0){
                    result=Math.floor(result)
                }else if(result<0){
                    result=Math.ceil(result)
                }
            }
            
            stack.push(result)
            
        }else{
            stack.push(token)
            
        }
    }
    return result
};
