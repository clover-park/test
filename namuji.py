num = []

for i in range(10):
    n = int(input('숫자: '))
    namuji = divmod(n, 42)
    num.append(namuji)

num = set(num)
print(len(num))