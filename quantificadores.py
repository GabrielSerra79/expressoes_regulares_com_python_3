# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem vem veeemmmmm"!
On3bs On4bs On56s
Jã, Jão
'''

print('Meta "+" com flag.IGNORECASE = ',
      re.findall(r'jo+ão', texto, flags=re.I))
print('Meta "+" com flag.IGNORECASE = ',
      re.findall(r'jo+ão+', texto, flags=re.I))
print('Meta "*" com flag.IGNORECASE = ',
      re.findall(r'jo*ão*', texto, flags=re.I))
print('Meta "?" com flag.IGNORECASE = ',
      re.findall(r'jo?ão?', texto, flags=re.I))
print('Meta "{}" com flag.IGNORECASE = ',
      re.findall(r've{3}m{1,2}', texto, flags=re.I))

texto2 = 'João ama ser amado'
print('Meta "{}" com flag.IGNORECASE = ',
      re.findall(r'ama[od]{0,2}', texto2, flags=re.I))

print('Sub -> Meta "+" com flag.IGNORECASE = ',
      re.sub(r'jo+ão+', 'GABIRU', texto, flags=re.I))
