"""
x: 최대공약수
y: 최소공배수
"""

n, m = map(int, input().split())

min_ = min(m,n)
max_ = max(m,n)

x = 0

for i in range(1, min_+1):
    if max_ % i==0 and min_ % i ==0:
        x = i

y = int(max_ / x * min_)

print(x)
print(y)