m1=str({})
m2=str({})
m3=str({})
kolvo=0
def nomer(x):
    nom=str({k})
    nom=nom+'_'
    nom=nom+x[0]
    nom=nom+'_'
    sch=0
    nomsch=0
    for i in range(0,len(x)):
        if x[i]==' ':
            nomsch=i
            break
    for i in range(nomsch+1,len(x)):
        sch=sch+1
    nom=nom+str(sch)
    print(nom)
    return(x)   
print('Введите участников олимпиады по математике, при завершении введите "конец"')
while True:
    a=input()
    x=a
    k=0
    if a!='конец':
        m1=m1+a
        k=k+1
        kolvo=kolvo+1
        nomer(x)
    else:
        print('Введите участников олимпиады по информатике, при завершении нажмите "конец"')
        b=input()
        x=b
        if b!='конец':
            m2=m2+b
            k=k+1
            kolvo=kolvo+1
            nomer(x)
        else:
            print('Введите участников олимпиады по физике, при завершении нажмите "конец"')
            c=input()
            x=c
            if c!='конец':
                m3=m3+c
                k=k=1
                kolvo=kolvo+1
                nomer(x)
            else:
                print('Работа завершена')
                break
print(kolvo)                        