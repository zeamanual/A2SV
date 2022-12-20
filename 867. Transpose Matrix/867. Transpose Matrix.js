/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function (matrix) {
    let row = matrix.length
    let colm = matrix[0].length
    let newArray = new Array(colm).fill(0).map(ele => new Array(row).fill(0))
    for (let rowIndex = 0; rowIndex < row; rowIndex++) {
        for (let columnIndex = 0; columnIndex < colm; columnIndex++) {
            newArray[columnIndex][rowIndex] = matrix[rowIndex][columnIndex]
        }
    }
    return newArray
};
