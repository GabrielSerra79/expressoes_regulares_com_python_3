# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> borda
# \B -> não borda
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
# print(re.findall(r'[a-z]+', texto, flags=re.I))
# # ['Jo', 'o', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', 'de', 'janeiro', 'de', 'Maria', 'era', 'o', 'nome', 'dela', 'Foi', 'um', 'ano', 'excelente', 'na', 'vida', 'de', 'jo', 'o', 'Teve', 'ALGO', 'filhos', 'todos', 'adultos', 'atualmente', 'maria', 'hoje', 'sua', 'esposa', 'ainda', 'faz', 'aquele', 'caf', 'com', 'p', 'o', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo', 'Tamb', 'm', 'n', 'Sendo', 'a', 'boa', 'mineira', 'que', 'nunca', 'esquece', 'seu', 'famoso', 'p', 'o', 'de', 'queijo', 'N', 'o', 'canso', 'de', 'ouvir', 'a', 'Maria', 'Jooooooooo', 'ooooooo', 'o', 'caf', 't', 'prontinho', 'aqui', 'Veeemm']

# print(re.findall(r'[a-zA-Z]+', texto))
# # ['Jo', 'o', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', 'de', 'janeiro', 'de', 'Maria', 'era', 'o', 'nome', 'dela', 'Foi', 'um', 'ano', 'excelente', 'na', 'vida', 'de', 'jo', 'o', 'Teve', 'ALGO', 'filhos', 'todos', 'adultos', 'atualmente', 'maria', 'hoje', 'sua', 'esposa', 'ainda', 'faz', 'aquele', 'caf', 'com', 'p', 'o', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo', 'Tamb', 'm', 'n', 'Sendo', 'a', 'boa', 'mineira', 'que', 'nunca', 'esquece', 'seu', 'famoso', 'p', 'o', 'de', 'queijo', 'N', 'o', 'canso', 'de', 'ouvir', 'a', 'Maria', 'Jooooooooo', 'ooooooo', 'o', 'caf', 't', 'prontinho', 'aqui', 'Veeemm']

# print(re.findall(r'[a-zA-Z0-9]+', texto))
# # ['Jo', 'o', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', '10', 'de', 'janeiro', 'de', '1970', 'Maria', 'era', 'o', 'nome', 'dela', 'Foi', 'um', 'ano', 'excelente', 'na', 'vida', 'de', 'jo', 'o', 'Teve', 'ALGO', '5', 'filhos', 'todos', 'adultos', 'atualmente', 'maria', 'hoje', 'sua', 'esposa', 'ainda', 'faz', 'aquele', 'caf', 'com', 'p', 'o', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo', 'Tamb', 'm', 'n', 'Sendo', 'a', 'boa', 'mineira', 'que', 'nunca', 'esquece', 'seu', 'famoso', 'p', 'o', 'de', 'queijo', 'N', 'o', 'canso', 'de', 'ouvir', 'a', 'Maria', 'Jooooooooo', 'ooooooo', 'o', 'caf', 't', 'prontinho', 'aqui', 'Veeemm']

# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# # ['João', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', '10', 'de', 'janeiro', 'de', '1970', 'Maria', 'era', 'o', 'nome', 'dela', 'Foi', 'um', 'ano', 'excelente', 'na', 'vida', 'de', 'joão', 'Teve', 'ALGO', '5', 'filhos', 'todos', 'adultos', 'atualmente', 'maria', 'hoje', 'sua', 'esposa', 'ainda', 'faz', 'aquele', 'café', 'com', 'pão', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo', 'Também', 'né', 'Sendo', 'a', 'boa', 'mineira', 'que', 'é', 'nunca', 'esquece', 'seu', 'famoso', 'pão', 'de', 'queijo', 'Não', 'canso', 'de', 'ouvir', 'a', 'Maria', 'Joooooooooãooooooo', 'o', 'café', 'tá', 'prontinho', 'aqui', 'Veeemm']

print('Shorthand "w+" =', re.findall(r'\w+', texto, flags=re.I))
# Shorthand "w+" = ['João', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', '10', 'de', 'janeiro', 'de', '1970', 'Maria', 'era', 'o', 'nome', 'dela', 'Foi', 'um', 'ano', 'excelente', 'na', 'vida', 'de', 'joão', 'Teve_ALGO', '5', 'filhos', 'todos', 'adultos', 'atualmente', 'maria', 'hoje', 'sua', 'esposa', 'ainda', 'faz', 'aquele', 'café', 'com', 'pão', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo', 'Também', 'né', 'Sendo', 'a', 'boa', 'mineira', 'que', 'é', 'nunca', 'esquece', 'seu', 'famoso', 'pão', 'de', 'queijo', 'Não', 'canso', 'de', 'ouvir', 'a', 'Maria', 'Joooooooooãooooooo', 'o', 'café', 'tá', 'prontinho', 'aqui', 'Veeemm']

print('Shorthand "W+" =', re.findall(r'\W+', texto, flags=re.I))
# Shorthand "W+" = ['\n', ' ', '    ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ',\n', ' ', ' ', ' ', ' ', '.\n\n\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '. ', ' ', ' ', ', ', ' ', ' ', '.\n', ', ', ' ', ' ', ', ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', '. ', ' ', '! ', ' ', ' ', ' ', ' ', ' ', ', ', ' ', ' ', ' ', '\n', ' ', ' ', '.\n', ' ', ' ', ' ', ' ', ' ', ':\n"', ', ', ' ', ' ', ' ', ' ', '. ', '"!\n']

print('Shorthand "d+" =', re.findall(r'\d+', texto, flags=re.I))
# Shorthand "d+" = ['10', '1970', '5']

print('Shorthand "D+" =', re.findall(r'\D+', texto, flags=re.I))
# Shorthand "D+" = ['\nJoão trouxe    flores para sua amada namorada em ', ' de janeiro de ', ',\nMaria era o nome dela.\n\n\nFoi um ano excelente na vida de joão. Teve_ALGO ', ' filhos, todos adultos atualmente.\nmaria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de\ndomingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso\npão de queijo.\nNão canso de ouvir a Maria:\n"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!\n']

print('Shorthand "s+" =', re.findall(r'\s+', texto, flags=re.I))
# Shorthand "s+" = ['\n', ' ', '    ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', '\n\n\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '\n']

print('Shorthand "S+" =', re.findall(r'\S+', texto, flags=re.I))
# Shorthand "S+" = ['João', 'trouxe', 'flores', 'para', 'sua', 'amada', 'namorada', 'em', '10', 'de', 'janeiro', 'de', '1970,', 'Maria', 'era', 'o', 'nome', 'dela.', 'Foi', 'um', 'ano', 'excelente', 'na', 'vida', 'de', 'joão.', 'Teve_ALGO', '5', 'filhos,', 'todos', 'adultos', 'atualmente.', 'maria,', 'hoje', 'sua', 'esposa,', 'ainda', 'faz', 'aquele', 'café', 'com', 'pão', 'de', 'queijo', 'nas', 'tardes', 'de', 'domingo.', 'Também', 'né!', 'Sendo', 'a', 'boa', 'mineira', 'que', 'é,', 'nunca', 'esquece', 'seu', 'famoso', 'pão', 'de', 'queijo.', 'Não', 'canso', 'de', 'ouvir', 'a', 'Maria:', '"Joooooooooãooooooo,', 'o', 'café', 'tá', 'prontinho', 'aqui.', 'Veeemm"!']

print('Shorthand "be w+" =', re.findall(r'\be\w+', texto, flags=re.I))
# Shorthand "be w+" = ['em', 'era', 'excelente', 'esposa', 'esquece']

print('Shorthand "w+e b" =', re.findall(r'\w+e\b', texto, flags=re.I))
# Shorthand "w+e b" = ['trouxe', 'de', 'de', 'nome', 'excelente', 'de', 'atualmente', 'hoje', 'aquele', 'de', 'de', 'que', 'esquece', 'de', 'de']

print('Shorthand "b w{4} b" =', re.findall(r'\b\w{4}\b', texto, flags=re.I))
# Shorthand "b w{4} b" = ['João', 'para', '1970', 'nome', 'dela', 'vida', 'joão', 'hoje', 'café', 'café', 'aqui']

print('Shorthand "w{4}" =', re.findall(r'\w{4}', texto, flags=re.I))
# Shorthand "w{4}" = ['João', 'trou', 'flor', 'para', 'amad', 'namo', 'rada', 'jane', '1970', 'Mari', 'nome', 'dela', 'exce', 'lent', 'vida', 'joão', 'Teve', '_ALG', 'filh', 'todo', 'adul', 'atua', 'lmen', 'mari', 'hoje', 'espo', 'aind', 'aque', 'café', 'quei', 'tard', 'domi', 'Tamb', 'Send', 'mine', 'nunc', 'esqu', 'famo', 'quei', 'cans', 'ouvi', 'Mari', 'Jooo', 'oooo', 'ooão', 'oooo', 'café', 'pron', 'tinh', 'aqui', 'Veee']

print('Shorthand "flores B" =', re.findall(r'flores\B', texto, flags=re.I))
# Shorthand "flores B" = []
