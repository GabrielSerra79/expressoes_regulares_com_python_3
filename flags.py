# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall \n
import re

texto = '''
131.768.460-53
055.123.060-50
955.123.060-90
'''

print('Flag "re.MULTILINE" =', re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))
# Flag "re.MULTILINE" = ['131.768.460-53', '055.123.060-50', '955.123.060-90']

texto2 = '''O João gosta de folia
E adora ser amado'''
print('Flag "re.IGNORECASE | re.S" =', re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
# Flag "re.IGNORECASE | re.S" = ['O João gosta de folia\nE adora ser amado']
