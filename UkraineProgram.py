from itertools import zip_longest

"""нет никакой возможности понять что тут происходит. различные a, f, b, i выполняют роль обфускации."""
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

 """можно единоразово запустить функцию без цикла"""
# while(1):
     """кончайте со своими шутками"""
#     print("введите \"слава украине\":",end=" ")
#     s = str(input())
    
     """узнать наличие чего-либо в строке возможно по помощи if a in b:, что полностью покрывает заявленный функионал, кроме 
     побуквенного нахождения ошибок, в котором нет необходимости."""
        
#     x = WordErrorC("слава украине",s.lower())
#     if x <= 2:
#         print("героям слава")
#         print("с новым годом")
#         break
#     print("вы допустили",x,"ошибок в фразе \"слава украине\", попробуйте ещё раз\n")

# input()

def compare(str1, str2):

    counter, mistakes = 0, 0
    str1, str2 = max([str1, str2], key=len), min([str1, str2], key=len)

    for e in str1:
        if counter+1>len(str2):
            break
        if e != str2[counter]:
            mistakes+=1
        counter+=1

    mistakes+=(len(str1)-len(str2))
    return mistakes

def compare_2(str1, str2):
    
    mistakes = 0
    for x, y in zip_longest(str1, str2):
        if x != y:
            mistakes+=1
    return mistakes

print('Please input something: ')
uinput, word = input(), '❄️🍉❄️'

"""функции похожи, вторая использует импортируемый zip_longest"""
mistakes, mistakes2 = compare(uinput, word), compare_2(uinput, word)
print(f'We compared {uinput} to {word} and found {mistakes, mistakes2} mistakes.')
if not mistakes|mistakes2:
    print('Have a happy new year!')

"""Действительно верное решение: """
if uinput == word:
    print('❄️🍉❄️🍉❄️🍉❄️🍉')
