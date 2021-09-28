def fac_using_recursive(n):
    if n==0:
        return 1
    else:
        return n*fac_using_recursive(n-1)

#0!=1
#n!=n*(n-1)!
#재귀함수:함수 내부에서 함수를 호출