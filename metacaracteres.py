# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

# # Saida

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
On3bs On4bs On56s
'''

print('Meta caractere ou "|" = ', re.findall(r'João|Maria|todos', texto))
# Meta caractere ou "|" =  ['João', 'Maria', 'todos', 'Maria']

print('Meta caractere qualquer "." = ', re.findall(r'On.bs', texto))
# Meta caractere qualquer "." =  ['On3bs', 'On4bs']

print('Meta caractere qualquer "." = ', re.findall(r'On..s', texto))
# Meta caractere qualquer "." =  ['On3bs', 'On4bs', 'On56s']

print('Meta conjunto "[]" = ', re.findall(r'[Jj]oão|[Mm]aria', texto))
# Meta conjunto "[]" =  ['João', 'Maria', 'joão', 'maria', 'Maria']

print('Meta conjunto "[]" com range "-" = ', re.findall(r'[a-z]aria', texto))
# Meta conjunto "[]" com range "-" =  ['maria']

print('Meta conjunto "[]" com range "-" = ',
      re.findall(r'[a-zA-Z]aria', texto))
# Meta conjunto "[]" com range "-" =  ['Maria', 'maria', 'Maria']

print('flag.IGNORECASE = ',
      re.findall(r'jOãO|MArIa', texto, flags=re.I))
# flag.IGNORECASE =  ['João', 'Maria', 'joão', 'maria', 'Maria']
