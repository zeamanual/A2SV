/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function (chars) {
    if (chars.length < 2) {
        return 1
    }

    let index = 0
    let totoalChars = chars.length
    let leftPtr = 0
    console.log(chars.length)
    let rightPtr = 1

    while (rightPtr <= totoalChars) {
        if (chars[leftPtr] == chars[rightPtr]) {
            rightPtr += 1
        } else {
            chars[index] = chars[leftPtr]
            index += 1
            let currentLength = rightPtr - leftPtr
            if (currentLength >= 10) {
                let formated = `${Math.floor(currentLength / 10)}`
                for (let ch of formated) {
                    chars[index] = ch
                    index+=1
                }
                chars[index] = `${currentLength % 10}`
                index += 1
            } else if (currentLength > 1) {
                chars[index] = `${currentLength}`
                index += 1
            }
            leftPtr = rightPtr
            rightPtr += 1
        }
    }
    return index
};
