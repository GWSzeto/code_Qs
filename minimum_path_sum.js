/**
 * @param {number[][]} grid
 * @return {number}
 */
const minPathSum = grid => {
    const leastPath = grid.reduce((acc, row, i) => {
        if (i == 0) {
            const newAcc = row.reduce((sumAcc, value, i) => {
                if (sumAcc.length == 0) return [...sumAcc, value]
                return [...sumAcc, value + sumAcc[sumAcc.length - 1]]
            }, [])

            return newAcc
        }

        const newAcc = row.reduce((sumAcc, value, i) => {
            if (i == 0) return [value + sumAcc[0], ...sumAcc.slice(1)]
            const minimumPath = sumAcc[i] < sumAcc[i - 1] ? sumAcc[i] : sumAcc[i - 1]
            const newPath = minimumPath + value
            if (i == sumAcc.length - 1) return [...sumAcc.slice(0, -1), newPath]
            return [...sumAcc.slice(0, i), minimumPath + value, ...sumAcc.slice(i + 1)]
        }, acc)
        
        return newAcc
    }, [])

    return leastPath[leastPath.length - 1]
}
