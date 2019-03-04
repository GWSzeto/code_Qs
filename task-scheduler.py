import collections
import heapq
def leastInterval(tasks, n):
    task_freqs = collections.Counter(tasks)
    task_freqs = [[val, key] for key, val in task_freqs.items()]
    heapq._heapify_max(task_freqs)

    time = 0
    while len(task_freqs) != 0:
        i = 0
        temp = []
        while i <= n:
            if task_freqs:
                task = heapq._heappop_max(task_freqs)
                task[0] -= 1
                if task[0] > 0:
                    temp.append(task)
            time += 1
            if not task_freqs and not temp:
                break
            i += 1
        task_freqs += temp
        heapq._heapify_max(task_freqs)

    return time

    


