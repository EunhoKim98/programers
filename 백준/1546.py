num = int(input())
score = list(map(int, input().split(' ')))
_sum = sum(score)
_max = max(score)

print(_sum*100/_max/num)
