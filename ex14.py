#O Maior
lista = input().split()
A = int(lista[0])
B = int(lista[1])
C = int(lista[2])

#abs na formula é numero absoluto
maiorab = (A+B+abs(A-B)) / 2
maiorab = int(maiorab)

if maiorab > C:
    print(maiorab,' eh o maior')
else:
    print(C,' eh o maior')