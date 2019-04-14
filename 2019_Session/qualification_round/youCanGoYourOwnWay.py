T = int(input())

def transform(P):
    ans = ""
    for w in P:
        if w == "S":
            ans += "E"
        else:
            ans += "S"
    return ans

for i in range(1, T+1):
    N = int(input())
    P = input()
    
    ans = transform(P)
    print("Case #{}: {}".format(i, ans))
