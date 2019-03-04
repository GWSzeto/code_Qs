from collections import defaultdict
def uncommonFromSentences(A, B):
    A_list = A.split(" ")
    B_list = B.split(" ")
    word_count = defaultdict(int)
    for word in A_list:
        word_count[word] += 1
    for word in B_list:
        word_count[word] += 1

    return [word for word, count in word_count.items() if count == 1]

print(uncommonFromSentences("this apple is sweet", "this apple is sour"))
        
