let rivers = [];

let riverSizes = (matrix) => {
    for (let j = 0; j < matrix.length; j++) {
        for (let i = 0; i < matrix[j].length; i++) {
            if (checkUsed(i, j) || !(matrix[j][i]))
                continue;
            let new_river = [];
            rivers.push(new_river);
            checkNeighbors(i, j, matrix, new_river);
        }
    }
    let sizes = rivers.map(i => i.length);
    rivers = [];
    return sizes;
}

let checkUsed = (i, j) => {
    for (let river of rivers) {
        for (let indexes of river) {
            if (indexes[0] == i && indexes[1] == j)
                return true;
        }
    }
    return false;
}

let checkNeighbors = (i, j, matrix, river) => {
    if (checkUsed(i, j))
        return
    river.push([i, j]);
    if (i > 0 && matrix[j][i - 1])
        checkNeighbors(i - 1, j, matrix, river);
    if (j > 0 && matrix[j - 1][i])
        checkNeighbors(i, j - 1, matrix, river);
    if (i < matrix[j].length - 1 && matrix[j][i + 1])
        checkNeighbors(i + 1, j, matrix, river);
    if (j < matrix.length - 1 && matrix[j + 1][i])
        checkNeighbors(i, j + 1, matrix, river);
}

// Do not edit the line below.
exports.riverSizes = riverSizes;