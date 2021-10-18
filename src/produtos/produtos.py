from abc import ABC, abstractmethod
from datetime import datetime

class Produtos(ABC):
    def __init__(self, nome, marca, data_venc, quantidade, preco):
        self._nome= nome
        self._marca= marca
        self._quantidade= quantidade
        self._data_venc= data_venc
        self._data= datetime.now()
        self._preco = preco
    
    @property
    def nome(self):
        return self._nome
    
    def nome(self, nome):
        self._nome= nome
    @property 
    def preco(self):
        return self._preco

    def preco(self, preco):
        if( preco <= 0):
            print("Valor invalido")
            return False
        self._preco = preco
    
    def marca(self):
        return self._marca
    def addmarca(self, marca):
        self._marca= marca

    @property 
    def quantitade(self):
        return self._quantidade

    def quantitade(self, quantidade):
        if( quantidade <= 0):
            print("Valor invalido")
            return
        self._quantidade += quantidade

    def menos_quantidade(self):
        self._quantidade= self._quantidade-1
    
    def data_venc(self):
        d1 = datetime.strptime(self._data_venc, '%d-%m-%Y')
        return d1

    
    def data_now(self):
        return self._data

    @property
    def print_basicos(self):
        print("nome: "+ self._nome)
        print("marca: "+ str(self._marca))
        print("preço: ", str(self._preco))
        print("data de validade: ", str(self._data_venc))
        print("quantidade: "+ str(self._quantidade))
    
    @abstractmethod
    def tipo_produto(self):
        pass
    def __str__(self):
        self.print_basicos()
        return
        

    