import re

# https://regex101.com/r/DfXYXM/1/
regexp = re.compile(r'^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4})$', flags=re.M)

texto = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''

for telefone in regexp.findall(texto):
    print('Telefone:', telefone)
    """ Saida
        Telefone: (21) 9 8852-5214
        Telefone: (35) 9 9975-4521
    """


regexp = re.compile(r'^(\(\d{2}\)\s)(9\s)(\d{4}-\d{4})$', flags=re.M)

for telefone in regexp.findall(texto):
    ddd, digito, numero = telefone
    print('DDD:', ddd)
    # #-> DDD: (21)
    # #-> DDD: (35)

    print('Digito:', digito)
    # #-> Digito: 9
    # #-> Digito: 9

    print('Numero:', numero)
    # #-> Numero: 8852-5214
    # #-> Numero: 9975-4521
