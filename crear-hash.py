'''
Crear un hash de ejemplo con Python 3.
Se usa la funcion SHA256 como prueba
Pasar como parámetro el path del archivo del cual obtener hast
Ejemplo: python3 crear-hash.py /path/al/archivo.zip
'''
import sys

f = open(sys.argv[1], 'rb')
file_bytes = f.read()
f.close()

import hashlib
m = hashlib.sha256()
m.update(file_bytes)
hash = m.hexdigest()
print('SHA256 del Documento: {}'.format(hash))
