import hashlib
import random
import time
from Transacao import Transacao

class Bloco:
    def __init__(self, transacoes, hash_anterior):
        self.transacoes = transacoes
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.timestamp = time.time()
        self.proof = None
        self.hash = self.gerar_hash()

    def gerar_hash(self):
        conteudo_bloco = str(self.transacoes) + str(self.hash_anterior) +  str(self.nonce) + str(self.timestamp) + str(self.proof)
        hash_bloco = hashlib.sha256(conteudo_bloco.encode()).hexdigest()
        return hash_bloco

    def minerar_bloco(self, dificuldade):
        while self.hash[:dificuldade] != '0' * dificuldade:
            self.proof = random.randint(0, 1000000)  # Número aleatório apenas para exemplo
            self.hash = self.gerar_hash()

    def __repr__(self):
        return f"Bloco({self.hash}, {self.hash_anterior}, {self.timestamp}, {self.transacoes})"