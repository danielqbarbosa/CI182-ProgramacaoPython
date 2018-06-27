# O jogo da alunissagem
# lunar.py
# importar funcao sqrt do modulo math
from math import sqrt

x = 500.    # altitude em pes
v = -50.    # velocidade em pes/s
g = -5. # aceleracao gravitacional lunar em pes/s/s
t = 1.  # tempo entre jogadas em segundos
comb = 120. # quantidade de combustível

print ('Simulacao de alunissagem')
print
print ('(digite a quantidade de combustivel a queimar)')

fmt = 'Alt: %6.2f  Vel: %6.2f  Comb: %3d'
while x > 0:    # enquanto nao tocamos o solo
    msg = fmt % (x, v, comb) # montar mensagem
    if comb > 0:        # ainda temos combustivel?
        # obter quantidade de combustivel a queimar
        resp = input(msg + ' Queima = ')
        try:    # converter resposta em numero
            queima = float(resp)
        except: # a resposta nao era um numero
            queima = 0
        if queima > comb: # queimou mais do que tinha?
            queima = comb # entao queima o que tem
        comb = comb - queima    # subtrai queimado
        a = g + queima    # acel = grav + queima
    else:    # sem combustivel
        print (msg)   # mensagem sem perguntar
        a = g   # aceleracao = gravidade
    x0 = x      # armazenar posicao inicial
    v0 = v      # armazenar velocidade inicial
    x = x0 + v0*t + a*t*t/2     # calc. nova posicao
    v = v0 + a*t                # calc. nova vel.

# se o loop acabou, tocamos no solo (x <= 0)
vf = sqrt(v0*v0 + 2*-a*x0)  # calcular vel. final
print ('>>>CONTATO! Velocidade final: %6.2f' % (-vf))

# avaliar pouso de acordo com a velocidade final
if vf == 0:
    msg = ('Alunissagem perfeita!')
elif vf <= 2:
    msg = ('Alunissagem dentro do padrao.')
elif vf <= 10:
    msg = ('Alunissagem com avarias leves.')
elif vf <= 20:
    msg = ('Alunissagem com avarias severas.')
else:
    msg = ('Modulo lunar destruido no impacto.')
print ('>>>' + msg)

# Como jogar
# Seu objetivo é desacelerar a nave, queimando combustível na dosagem certa ao longo da queda, para tocar o solo lunar com uma velocidade bem próxima de zero. Se você quiser, pode usar um diagrama como o mostrado abaixo (colocamos em nosso site um desses em branco, para você imprimir e usar). As unidades estão no sistema inglês, como no original. O mais importante é você saber que cada 5 unidades de combustível queimadas anulam a aceleração da gravidade. Se queimar mais do que 5 unidades, você desacelera; menos do que 5, você ganha velocidade. Primeiro, pratique seus pousos preocupando-se apenas com a velocidade final. Depois você pode aumentar a dificuldade, estabelecendo um limite de tempo: por exemplo, o pouso tem que ocorrer em exatos 13 segundos. Uma última dica: cuidado para não queimar combustível cedo demais. Se você subir, vai acabar caindo de uma altura ainda maior! Boas alunissagens!
