
var MinStack = function() {
    this.stack = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    let size = this.stack.length
    if(size<1){
        this.stack.push([val,val])
    }else{
        let last = this.stack.pop()
        let currentMinimum = last[1]
        this.stack.push(last)
        if(val<currentMinimum){
            this.stack.push([val,val])
        }else{
             this.stack.push([val,currentMinimum])
        }
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    let last = this.stack.pop()
    let required = last[0]
    return required
    
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    let last = this.stack.pop()
    let required = last[0]
    this.stack.push(last)
    return required
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    let last = this.stack.pop()
    let required = last[1]
    this.stack.push(last)
    return required
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
