# n = 1260
# count = 0
# conin_types = [500, 100, 50, 10]

# for coin in conin_types:
#     count += n // coin # n // coin -> (int)(n / coin) // 연사자는 나누기 후 소숫점 이하 자리는 버리고 정수만 취함
#     n %= coin

# print(count)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #오름차순으로 정렬
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -=1
    if m == 0:
        break
    result += second
    m -=1

print(result)