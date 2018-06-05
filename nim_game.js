/**
 * @param {number} n
 * @return {boolean}
 */
const canWinNim = n => {
    if (n % 4 != 0) return true
    return false
}