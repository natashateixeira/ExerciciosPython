#Cálculo Simples
P1 = input().split()
P2 = input().split()
#split() separa os valores recebidos conforme sua respectiva posição
cod1 = int(P1[0])
num1 = int(P1[1])
val1 = float(P1[2])
cod2 = int(P2[0])
num2 = int(P2[1])
val2 = float(P2[2])

total = (val1 * num1) + (val2 * num2)

print (f'VALOR A PAGAR: R$ {total:.2f}')