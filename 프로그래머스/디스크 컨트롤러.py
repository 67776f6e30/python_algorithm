import heapq


def solution(jobs):
    time = 0
    avg = 0
    job_list = sorted(jobs, reverse=True)
    heap = []
    while job_list or heap:
        if job_list and job_list[-1][0] >= time:
            job = job_list.pop()
            time += job[1]
            avg += time - job[0]
        else:
            while job_list:
                if job_list[-1][0] < time:
                    job = job_list.pop()
                    heapq.heappush(heap, (time - job[0], (job[1], job[0])))
                else:
                    break
            job = heapq.heappop(heap)[1]
            time += job[0]
            avg += time - job[1]

    return avg // len(jobs)


data = [
    (i, i + 1) for i in range(10)
]
print(solution([[0, 3], [1, 9], [2, 6]]))
