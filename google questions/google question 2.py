def solution(S, T):
    # write your code in Python 3.6

    s_index = 0

    for letter in T:
        if s_index >= len(S): 
            return 0
        while s_index < len(S) and S[s_index] != letter:
            s_index += 1
        # adding another 1 to move off of the matching letter
        s_index += 1
    
    return 1
