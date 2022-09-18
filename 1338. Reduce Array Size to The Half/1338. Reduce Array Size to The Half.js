/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
    let minimumSize=0
    let removedAmount =0
    let arraySize = arr.length
    let frequencyCount ={}
    for(let number of arr){
        if(frequencyCount[number]===undefined){
            frequencyCount[number]=1
        }else{
            frequencyCount[number]+=1
        }
    }
    
    let listFrequencyCount=[]
    for (let id in frequencyCount){
        let temp =[]
        temp.push(id)
        temp.push(frequencyCount[id])
        listFrequencyCount.push(temp)
    }
    
    listFrequencyCount.sort((a,b)=>{
        return b[1]-a[1]
    })
    
    for (let number of listFrequencyCount ){
        if(removedAmount>= Math.floor(arraySize/2)){
            break

        }else{
            minimumSize+=1
            removedAmount+=number[1]
        }
    }
    
    return minimumSize


};
