def wordPattern(pattern, str):
    pattern_map = {}
    word_map = {}
    words = str.split(" ")

    if not len(words) == len(pattern):
        return False

    for i in range(len(words)):
        if pattern[i] not in pattern_map:
            pattern_map[pattern[i]] = words[i]
        if not pattern_map[pattern[i]] == words[i]:
            return False
        if words[i] not in word_map:
            word_map[words[i]] = pattern[i]
        if not word_map[words[i]] == pattern[i]:
            return False
          
    return True

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))
print(wordPattern("abba", "dog dog dog dog"))

