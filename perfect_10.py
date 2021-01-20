def sum10(n):
    perf=[]
    x=0
    while len(perf)<n:
        if sum([int(a) for a in str(x)])==10: perf.append(x)
        x+=1       
    return perf[n-1]

print(sum10(3))