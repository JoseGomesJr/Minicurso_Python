from .produtos import Produtos

class Bebidas(Produtos):
    def __init__(self, nome, marca, data_venc, volume, quantidade, preco):
        super().__init__(nome, marca, data_venc, quantidade, preco)
        self._volume= volume
    
    @property 
    def volume(self):
        return self._volume
    def addpeso_volume(self, volume):
        if( volume <= 0):
            print("Valor invalido")
            return False
        self._volume= volume
        return True

    @property
    def print(self):
        print("volume: ", str(self._volume))
    
    def tipo_produto(self):
        return "Bebida"
    def __str__(self):
        self.print_basicos
        self.print
        return '\n'