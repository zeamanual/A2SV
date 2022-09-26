/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
 var validateStackSequences = function(pushed, popped) {
    let stack = []
    let isValid = true
    let ptOne = 0
    let ptTwo = pushed.length-1
    
    
    for (let popedValue of popped){
        if(stack.includes(popedValue) ){
            let tempPoped = stack.pop() 
            while(tempPoped !== popedValue){
                tempPoped = stack.pop()
            }
            continue
        }else if(ptOne<=ptTwo){
                let toBePushed = pushed[ptOne]
                while (toBePushed !==popedValue){
                    stack.push(pushed[ptOne])
                    if(ptOne<ptTwo){
                        ptOne+=1
                        toBePushed = pushed[ptOne]                          
                    }else{
                        break
                    }

                }
                
                if(toBePushed==popedValue){
                    ptOne+=1
                    continue
                }else{
                    isValid=false
                    break
                }
                
            }else{
                isValid=false
                break
            }
    }
    
    return isValid
};
