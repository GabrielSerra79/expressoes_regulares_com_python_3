# https://regex101.com/r/W4kRV2/2/
# https://en.wikipedia.org/wiki/List_of_Unicode_characters
import re
senha_forte_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)

string = '''
VÁLIDAS
]n;ZGVy{188b
4m`UJp@6Uw8%
6;ceNc05}QA^
9F}w65+q}HMc
B>p~5Nvi3?O4

SEM MINÚSCULAS
Q2NV*1>:7]K9
X8W{6|W~?9Y7
2@<Z9>?R36TX
?F\38A2NA{7\
IQJ9_7|9__0R

SEM MINÚSCULAS E NÚMEROS
IZ,L/:.B<-HS
;GD_}D}$WAI$
{DC'&SCE{{`R
F;DS:L<?IG-"
G~S{M{|W?O>A

SEM NÚMEROS CARACTERES E MINÚSCULAS
AHFFBZXDSYDR
BHLQXQRXRQHA
UVDIRIABCRKV
VMXHTDATRQDQ
PBJSQAUDXNDX

MAIUSCULAS E MINUSCULAS
GltZFGmDtjBs
qJvrBJMzHyyW
UqpvNlkAlOJR
AIXuirGRaiRx
jlseVICPqMxF

MAIUSCULAS, MINUSCULAS e NUMEROS
GOzV731iPx7w
3B7mdR4YGd5v
fJMu9aU769Hb
4DE4b7jLdz1R
dx8lBzEA53J1

QUANTIDADE INVÁLIDA (6)
pd0]1K
G0]lo8
x7|J9g
Ke0b>2
8Z3^lw
'''

print('Senhas validas:', senha_forte_regexp.findall(string))
# #-> Senhas validas: [']n;ZGVy{188b', '4m`UJp@6Uw8%', '6;ceNc05}QA^', '9F}w65+q}HMc', 'B>p~5Nvi3?O4']
