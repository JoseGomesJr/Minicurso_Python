from .produtos import Produtos

class Higiene(Produtos):
    def __init__(self, nome, marca, data_venc, volume, quantidade, preco):
        super().__init__(nome, marca, data_venc, quantidade, preco)
        self._volume= volume
        self._unidade= ""
    
    @property 
    def volume(self):
        return self._volume
    def addvolume(self, volume, unidade):
        if volume <= 0 and unidade != "ml" or unidade != 'g':
            print("Valor invalido ou unidade invalidos")
            return False
        self._volume= volume
        self._unidade= unidade
        return True
    @property
    def print(self):
        print("volume\peso do produto: ", str(self._volume))
    
    def tipo_produto(self):
        return "Higiene"
    def __str__(self):
        self.print_basicos
        self.print
        return '\n'