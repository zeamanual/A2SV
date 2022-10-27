/**
 * @param {number[]} arr
 * @return {number}
 */
var longestMountain = function (arr) {

    let mountainStates = Object.freeze({
        NOT_INSIDE: 'NOT-INSIDE',
        UP: 'UP',
        DOWN: 'DOWN'
    })
    let currentMountainState = mountainStates.NOT_INSIDE
    let leftPtr = 0
    let rightPtr = 1
    let answer = 0
    let arraySize = arr.length

    while (rightPtr < arraySize) {
        console.log(leftPtr, rightPtr, currentMountainState)
        if (arr[rightPtr] > arr[rightPtr - 1]) {
            if (currentMountainState === mountainStates.DOWN) {
                let tempMax = rightPtr - leftPtr
                answer = Math.max(tempMax, answer)
                leftPtr = rightPtr - 1
                currentMountainState = mountainStates.UP
            } else {
                currentMountainState = mountainStates.UP
            }
        } else if (arr[rightPtr] === arr[rightPtr - 1]) {
            if (currentMountainState === mountainStates.DOWN) {
                let tempMax = rightPtr - leftPtr
                answer = Math.max(tempMax, answer)
            }
            leftPtr = rightPtr
            currentMountainState = mountainStates.NOT_INSIDE
        } else {
            if (currentMountainState === mountainStates.UP) {
                currentMountainState = mountainStates.DOWN
            } else if (currentMountainState !== mountainStates.DOWN) {
                leftPtr = rightPtr
            }
        }
        rightPtr += 1
    }

    if (currentMountainState === mountainStates.DOWN) {
        let tempMax = rightPtr - leftPtr
        answer = Math.max(answer, tempMax)
    }
    return answer


};
