# Aplicar funciones hash a un documento

Aplicar una [función hash](https://es.wikipedia.org/wiki/Funci%C3%B3n_hash) a un documento es una forma de obtener un identificador _único_ del archivo muy pequeño.  

Es muy útil para certificar que un documento no ha sido modificado.

En caso de que el documento use funciones hash como SHA256 se puede replicar con [este código](crear-hash.py) que acompañamos.  
Si el documento fue procesado con [OpenTimeStamps](https://opentimestamps.org/) puede usarse su [cliente abierto](https://github.com/opentimestamps/opentimestamps-client) para controlar.
