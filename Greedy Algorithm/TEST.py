n = 1260
count = 0
conin_types = [500, 100, 50, 10]

for coin in conin_types:
    count += (int)(n / coin)
    n %= coin

print(count)
