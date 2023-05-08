num = int(input('Numero: '))
antp = 0
pen = 1
ult = pen + antp
print(antp, ', ', pen, sep='', end='')
for i in range(2,num-1):   
    print(', ',ult, sep='', end='')
    antp=pen
    pen=ult
    ult = pen + antp
if (num>2):
    print(', ',ult,sep='')
