# n = 1260
# count = 0
# conin_types = [500, 100, 50, 10]

# for coin in conin_types:
#     count += n // coin # n // coin -> (int)(n / coin) // 연사자는 나누기 후 소숫점 이하 자리는 버리고 정수만 취함
#     n %= coin

# print(count)

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort() #오름차순으로 정렬
# first = data[n-1]
# second = data[n-2]

# result = 0


# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -=1
#     if m == 0:
#         break
#     result += second
#     m -=1

# count = int(m/(k+1)) * k
# count += m%(k+1)

# result += count * first
# result += (m-count) * second

# print(result)

# n, m = map(int, input().split())

# result = 0

# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)

# print(result)

# for i in range(n):
#     data = list(map(int, input().split()))

#     min_value = 10001 #max

#     for a in data:
#         min_value = min(min_value, a)

#     result = max(min_value, result)

# print(result)

n, k = map(int, input().split())

result = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n //= k
#     result += 1

# while n > 1:
#     n-=1
#     result += 1

# while True:
#     target = (n//k) * k
#     result += (n - target)

#     n = target

#     if n < k:
#         break

#     result += 1
#     n //= k

# result += (n-1)

# print(result)

while True:
    target = (n%k)
    result += target
    n -= target

    if n < k:
        result += (n-1)
        break

    result += 1
    n //= k

print(result)