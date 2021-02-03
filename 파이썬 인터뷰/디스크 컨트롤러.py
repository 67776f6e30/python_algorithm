import heapq
from collections import deque


def solution(jobs):
    jobs = deque(jobs)
    h = []
    q = []
    heapq.heapify(h)
    time = 0
    while jobs:
        job = jobs.popleft()
        if jobs[0] >= time:
            q.append(job)
            time += jobs[1]
        if job[0] <= time:
            while jobs:
                if jobs[0][0] <=