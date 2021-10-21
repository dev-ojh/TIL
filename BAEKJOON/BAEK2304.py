N = int(input())
height = [0]*1002
for i in range(N):
    L, H = map(int, input().split())
    height[L] = H
max_height=0
max_height_idx=0
for j in range(1001):
    if height[j] > max_height:
        max_height = height[j]
        max_height_idx = j
tmp = 0
tmp_idx = 0
result = 0
for i in range(0, max_height_idx+1):
    if height[i] > tmp:
        result += tmp * (i-tmp_idx)
        tmp = height[i]
        tmp_idx = i
    
tmp = 0
tmp_idx = 1001
for i in range(1001, max_height_idx-1, -1):
    if height[i]>tmp:
        result += tmp * (tmp_idx - i-1)
        tmp = height[i]
        tmp_idx = i+1
result += tmp * (tmp_idx - max_height_idx)
    
print(result)
