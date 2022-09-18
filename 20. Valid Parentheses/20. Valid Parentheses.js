/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stackImpl =[]
    let symbols={
        '(':')',
        '{':'}',
        '[':']'
    }
    
    for(let char of s){
        if(Object.keys(symbols).includes(char)){
            stackImpl.push(char)
            continue
        }else{
            lastOpened = stackImpl.pop()
            if( symbols[lastOpened] != char){
                return false
            }
        }
    }
    if(stackImpl.length>0){
        return false
    }else{
        return true
    }
};
