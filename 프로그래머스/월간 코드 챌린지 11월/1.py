def solution(a, b):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
    return sum


a = [1, 2, 3, 4]
b = [-3,-1,0,2]
print(solution(a, b))
