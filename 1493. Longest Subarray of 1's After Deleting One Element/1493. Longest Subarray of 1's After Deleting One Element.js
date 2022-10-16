/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function (nums) {

    if (nums.length == 1) {
        return 0
    }
    let elementRemoved = 0
    let windowStart = 0
    let windowEnd = 0
    let max = 0


    while (windowEnd < nums.length) {
        if (elementRemoved < 1 && nums[windowEnd] == 0) {
            elementRemoved += 1
        } else if (elementRemoved > 0 && nums[windowEnd] == 0) {
            while (nums[windowStart] !== 0) {
                windowStart += 1
            }
            windowStart += 1
        }
        let reduceBy = elementRemoved > 0 ? 1 : 0
        let tempLong = (windowEnd - windowStart + 1) - reduceBy
        if (tempLong > max) {
            max = tempLong
        }

        windowEnd += 1

    }
    return elementRemoved == 0 ? max - 1 : max

};
