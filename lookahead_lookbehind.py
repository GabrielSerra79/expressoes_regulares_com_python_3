import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# Positive lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))
# ['192.168.0.1', '192.168.0.3', '192.168.0.4', '192.168.0.6']

# Negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))
# ['192.168.0.2', '192.168.0.5']

# Positive lookahead
pprint(re.findall(r'(?=.*[^in]active).+', texto))
'''
['ONLINE  192.168.0.1 GHIJK active',
 'OFFLINE  192.168.0.3 GHIJK active',
 'ONLINE  192.168.0.4 GHIJK active',
 'OFFLINE  192.168.0.6 GHIJK active']
 '''

# Positive lookbehind
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# ['192.168.0.1', '192.168.0.4', '192.168.0.5']

# Negative lookbehind
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# ['192.168.0.2', '192.168.0.3', '192.168.0.6']

# Positive lookbehind
pprint(re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))
'''
['OFFLINE  192.168.0.2 GHIJK inactive',
 'OFFLINE  192.168.0.3 GHIJK active',
 'OFFLINE  192.168.0.6 GHIJK active']
'''

# Negative lookbehind
pprint(re.findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))
'''
['ONLINE  192.168.0.1 GHIJK active',
 'ONLINE  192.168.0.4 GHIJK active',
 'ONLINE  192.168.0.5 GHIJK inactive']
'''
