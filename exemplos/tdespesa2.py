#desprep1.py - calculo de despesas da republica

print ('Balanco de despesas da Republica Recanto Suico')
print
print ('(deixe um nome em branco para encerrar)')
print
total = 0
contas = {}
while 1:
    pessoa = input('Digite o nome da pessoa: ')
    if not pessoa: break
    while 1:
        resp = input('Quanto gastou %s? ' % pessoa)
        try:
            gasto = float(resp)
            break
        except:
            print ('Numero invalido.')
    contas[pessoa] = gasto
    total = total + gasto

num_pessoas = len(contas)
print
print ('Numero de pessoas: %d' % num_pessoas)
print ('Total de gastos: R$ %.2f' % total)
media = total/num_pessoas
print ('Gastos por pessoa: R$ %.2f' % media)
print
for nome in contas.keys():
    saldo = contas[nome] - media
    print ('Saldo de %s: %.2f' % (nome, saldo))
