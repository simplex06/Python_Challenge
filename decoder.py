def decoder(number):
    n = len(number)
    lst = [0 for i in range(n)]
    
    if number[0] != '0':
        lst[0] = 1
        print("d", lst)
    for i in range(1,n):
        tekhane = int(number[i])
        ikihane = int(number[i-1:i+1])
        if tekhane >= 1 and tekhane <= 9:
            lst[i] += lst[i-1]
            print("a", lst)
        if ikihane >= 10 and ikihane <= 26:
            if i-2 >= 0:
               lst[i] += lst[i-2]
               print("b", lst)
            else:
               lst[i] += 1
               print("c", lst)
    
    return lst[-1]


print(decoder("9191"))