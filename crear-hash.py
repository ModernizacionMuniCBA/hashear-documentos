'''
Crear un hash de ejemplo con Python 3.
Se usa la funcion SHA256 como prueba
'''

f = open('/path/al/archivo', 'rb')
file_bytes = f.read()
f.close()

import hashlib
m = hashlib.sha256()
m.update(file_bytes)
hash = m.hexdigest()
print('SHA256 del Documento: {}'.format(hash_mio))
