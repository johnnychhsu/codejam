T = int(input())

def find(N):
    record = []
    num = []
    while N > 0:
        r = N % 10
        if r != 4:
            record.append(r)
            num.append(1)
        else:
            record.append(2)
            num.append(2)
        N = N // 10 
    A = B = 0
    for i, n in enumerate(record):
        A += 10**i * n
        num[i] -= 1
        if num[i] > 0:
            B += 10**i * n
            num[i] -= 1
    return A, B

for i in range(1, T + 1):
    N = int(input())
    
    A, B = find(N)
    
    print("Case #{}: {} {}".format(i, A, B))
