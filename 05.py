p = int(input('Número primo: '))
div = 0
for i in range (1, p+1):
    if (p % i == 0):
        div += 1
if (div == 2):
    print('Primo')
else:
    print('Não é primo')
