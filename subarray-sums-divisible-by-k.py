def subarraysDivByK(A, K):
    solution = []
    first = 0
    second = 1
    while first < len(A):
        sub_sum = sum(A[first:second]) 
        if sub_sum % K:
            solution.append(sub_sum)
        if sub_sum < K / 2:
            second += 1
        if sub_sum >= K / 2:
            first += 1
    
    return solution

print(subarraysDivByK([4,5,0,-2,-3,1], 5))
