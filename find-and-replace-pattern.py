def findAndReplacePattern(words, pattern):
    solution = []
    for word in words:
        if len(word) != len(pattern): continue
        word_to_pattern = dict()
        pattern_to_word = dict()
        match = True
        for i in range(len(pattern)):
            if word[i] not in word_to_pattern:
                word_to_pattern[word[i]] = pattern[i]
            if pattern[i] not in pattern_to_word:
                pattern_to_word[pattern[i]] = word[i]
            if pattern_to_word[pattern[i]] != word[i] or  word_to_pattern[word[i]] != pattern[i]:
                match = False
                break
        if match:
            solution.append(word)

    return solution

print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
