m1={}
max=0
print('Введите участников олимпиады по математике, при завершении введите "конец"')
while True:
    k=0
    print('Введите имя участника')
    a=input()
    if a!='конец':
        print('Введите количество его баллов')
        b=int(input())
        k=k+1
        m1[b]=a
        if b>max:
            max=b
    else:
        print('Работа завершена')
        break
print('Участник с максимальным количеством баллов: ', m1[max])    