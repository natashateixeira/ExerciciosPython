#Salário com Bônus
nome = (input())
salario = float(input())
totalvendas = float(input())

total = (totalvendas * 0.15) + salario
print(f'TOTAL = {total:.2f}')