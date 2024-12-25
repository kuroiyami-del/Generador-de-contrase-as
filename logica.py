import random
import string


class Creador:
    def __init__(self):
        pass

    def contraRandom(self, largo):
        # lista_letras = "abcdefghijklmnñopqrstuvxyz"
        # lista_numeros = "1234567890"
        # lista_simbolos = "|°!""#$%&/()=?'¡¿´+{}-.,;:_[]*¨¬"

        suma = string.digits + string.ascii_letters + string.punctuation  # a

        contraseña = "".join(random.sample(suma, largo))

        return contraseña
