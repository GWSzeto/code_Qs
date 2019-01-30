import heapq
def frequencySort(s):
    freq_dict = dict()
    for char in s:
        if char not in freq_dict:
            freq_dict[char] = -1
        else:
            freq_dict[char] -= 1

    freq_list = [(value, key) for key, value in freq_dict.items()]
    heapq.heapify(freq_list)
    return "".join(["".join([char for _ in range(abs(value))]) for value, char in freq_list])

print(frequencySort("tree"))
