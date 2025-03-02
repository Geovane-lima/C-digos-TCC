import hashlib
import time
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

class Transacao:
    def __init__(self, remetente, destinatario, valor, chave_privada=None):
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor
        self.timestamp = time.time()
        self.chave_privada = chave_privada
        self.assinatura = None

    def assinar_transacao(self):
        if self.chave_privada is None:
            return "Chave privada não fornecida."
        else:
            h = SHA256.new(str(self).encode('utf-8'))
            assinador = PKCS1_v1_5.new(self.chave_privada)
            self.assinatura = assinador.sign(h)

    def esta_assinado(self):
        return self.assinatura is not None

    def __repr__(self):
        return f"Transacao({self.remetente}, {self.destinatario}, {self.valor}, {self.timestamp})"