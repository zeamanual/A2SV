/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    let sLength = s.length
    let pLength = p.length
    let result = []
    if(sLength<pLength){
        return result
    }

    let rightPtr= pLength-1
    let leftPtr = 0
    let sHashMap = {}
    let pHashMap = {}


    for (let i =0;i<pLength;i++){
        sHashMap[s[i]]=sHashMap[s[i]]!==undefined?sHashMap[s[i]]+1:1
        pHashMap[p[i]]=pHashMap[p[i]]!==undefined?pHashMap[p[i]]+1:1

    }

    while(rightPtr<sLength){
        if(compare(sHashMap,pHashMap)){
        result.push(leftPtr)
        }
        sHashMap[s[leftPtr]]-=1
        leftPtr+=1
        rightPtr+=1
        sHashMap[s[rightPtr]]=sHashMap[s[rightPtr]]!==undefined?sHashMap[s[rightPtr]]+1:1
    }

    return result
};

let compare = (s,p)=>{
    let isEqual = true
    for(let key of Object.keys(p)){
        if(s[key]===p[key]){
            continue
        }else{
            isEqual=false
            break
        }
    }

    return isEqual
}
