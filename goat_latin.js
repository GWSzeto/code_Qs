/**
 * @param {string} 
 * @return {string}
 */
const toGoatLatin = S => {
    const vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    const words = S.split(" ")
    const goatWords = words.map((word, i) => {
        let goatWord = word
        if (vowels.includes(word[0])) { 
            goatWord = goatWord + "ma"
        } else {
            const firstLetter = goatWord.slice(0, 1)
            goatWord = goatWord.slice(1) + firstLetter + "ma"
        }
        goatWord = goatWord + "a".repeat(i + 1)
        
        return goatWord
    })

    const goatSentence = goatWords.join(" ")

    return goatSentence
}
