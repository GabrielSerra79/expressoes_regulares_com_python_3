# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1

# # Saida

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
'''

print('Greedy com meta "+"= ', re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', texto))
# Greedy com meta "+"=  ['<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>']

print('Non-greedy com meta "+"=', re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))
# Non-greedy com meta "+"= ['<p>Frase 1</p>', '<p>Eita</p>', '<p>Qualquer frase</p>']

print('Greedy com meta "*"= ', re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))
# Greedy com meta "*"=  ['<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>']

print('Non-greedy com meta "*"=', re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))
# Non-greedy com meta "*"= ['<p>Frase 1</p>', '<p>Eita</p>', '<p>Qualquer frase</p>', '<div></div>']
