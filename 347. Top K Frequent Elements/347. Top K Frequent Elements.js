/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {

    let frequency = {}
    for (let number of nums){
        if(frequency[number]==undefined){
            frequency[number]=1
        }else{
            frequency[number]+=1
        }
    }
    
    let frequencyList = []
    for (let number in frequency){
        temp =[]
        temp[0]=parseInt(number)
        temp[1]=frequency[number]
        frequencyList.push(temp)
    }
    
    frequencyList.sort((a,b)=>{
      return (b[1]-a[1])
    })
    
    

    let result = frequencyList.slice(0,k)
    result = result.map(data=>data[0])
    return result
};
