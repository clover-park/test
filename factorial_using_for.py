def factorial_using_for(n):
  k = 1
  for i in range(1, n+1):
    k *= i
  return k

print(factorial_using_for(70000))

# 숙제 : 1 재귀
#        2 자바에서는 jdk 설치