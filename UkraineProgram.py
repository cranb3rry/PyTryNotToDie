def WordErrorC(a:str, b:str):
    """сколько было допущенно ошибок во втором слове что в итоге получилось первое"""

    f = [[0]*(len(b) + 1) for x in range(len(a) + 1)]

    for x in range(len(a) + 1):
        f[x][0] = x
    for x in range(len(b) + 1):
        f[0][x] = x

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                f[i+1][j+1] = f[i][j]
            else:
                f[i+1][j+1] = 1 + min(f[i+1][j], f[i][j+1], f[i][j])

    return f[-1][-1]

flag = True
while(flag):
    print("введите \"слава украине\":",end=" ")
    s = str(input())

    x = WordErrorC("слава украине",s.lower())
    if x <= 2:
        print("героям слава")
        print("с новым годом")
        break
    print("вы допустили",x,"ошибок в фразе \"слава украине\", попробуйте ещё раз\n")

input()
