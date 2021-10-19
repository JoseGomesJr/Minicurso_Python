from .produtos import Produtos

class Alimentos(Produtos):
    def __init__(self, nome, marca, data_venc, peso, quantidade, preco):
        super().__init__(nome, marca, data_venc, quantidade, preco)
        self._peso= peso
    
    
    def peso(self):
        return self._peso
    
    def addpeso_volume(self, peso):
        if( peso <= 0):
            print("Valor invalido")
            return False
        self._peso= peso
        return True
    
    def print(self):
        print("peso: ", str(self._peso))
    
    def tipo_produto(self):
        return "Alimento"
    def __str__(self):
        self.print_basicos()
        self.print()
        return '\n'
    