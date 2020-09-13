def solution(lis, key):
    a=[-1,-1]
    c=lis
    for keyi,i in enumerate(c):
        for keyj,j in enumerate(c):
            if sum(lis[keyi:keyj+1]) == key:
                return [keyi, keyj]
    return a