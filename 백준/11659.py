#구간 합.
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = [0]
temp = 0

for i in arr:
    temp = temp + i
    result.append(temp)

for i in range(M):
    a1, a2 = map(int, input().split())
    print(result[a2] - result[a1-1])

#그냥 구현 했을 때. 시간 초과로 인해 실패.
#N, M = list(map(int, input().split(' ')))
#arr = list(map(int,input().split(' ')))
#result = [None]*M
#for i in range(M):
#    a1, a2 = list(map(int, input().split(' ')))
#    result[i] = sum(arr[a1-1:a2])
#    
#
#for i in range(M):
#    print(result[i])
