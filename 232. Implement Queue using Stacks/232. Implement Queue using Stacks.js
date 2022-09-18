
var MyQueue = function() {
    this.queOne=[]
    this.queTwo=[]
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.queOne.push(x)
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    let poped = this.queOne.pop()
    while(poped!==undefined){
        this.queTwo.push(poped)
        poped=this.queOne.pop()
    }
    
    let required = this.queTwo.pop()

    poped = this.queTwo.pop()
    
    while(poped!==undefined){
    this.queOne.push(poped)
    poped=this.queTwo.pop()
    }
    
    return required
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    return this.queOne[0]
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    if(this.queOne.length>0){
        return false
    }else{
        return true
    }
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
