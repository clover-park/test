def binary(n):
    a, b = divmod(n, 2)
    binary_list.append(str(b))
    if a > 0 :
      binary(a)

def hexa(n):
  c,d = divmod(n, 16)
  if d == 10:
      hex_list.append('a')
  elif d == 11:
    hex_list.append('b')
  elif d == 12:
    hex_list.append('c')
  elif d == 13:
    hex_list.append('d')
  elif d == 14:
    hex_list.append('e')
  elif d == 15:
    hex_list.append('f')
  else:
    hex_list.append(str(d))
  if c > 0 :
    hexa(c)

while True:
  num = int(input('양의 정수 입력(음수입력시 종료): '))
  if num >= 0:
    binary_list = []
    binary(num)
    hex_list = []
    hexa(num)
    print(str(num) +'의 이진수:',''.join(binary_list[::-1]), end=' ')
    print()
    print(str(num) +'의 16진수:',''.join(hex_list[::-1]), end=' ')
    print()
  else:
    break
