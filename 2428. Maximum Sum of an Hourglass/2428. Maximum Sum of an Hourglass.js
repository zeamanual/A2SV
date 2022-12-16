/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxSum = function (grid) {
    let xStart = 0
    let rowCount = 0
    let sum = Number.NEGATIVE_INFINITY
    while (rowCount <= grid.length - 3) {
        xStart = 0
        while (xStart <= grid[0].length - 3) {
            tempSum = grid[rowCount][xStart] + grid[rowCount][xStart + 1] + grid[rowCount][xStart + 2] + grid[rowCount + 1][xStart + 1] + grid[rowCount + 2][xStart] + grid[rowCount + 2][xStart + 1] + grid[rowCount + 2][xStart + 2]
            sum = Math.max(sum, tempSum)
            xStart += 1
        }
        rowCount += 1
    }
    return sum
};
