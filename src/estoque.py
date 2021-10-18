from .utils import PrintInfo
from .produtos import *

class Estoque():
    estoques = {}
    id= 0

    @classmethod
    def addproduct(cls, produtos):
        cls.estoques[cls.id]= produtos
        cls.id= cls.id + 1
    @classmethod
    def remove(cls, posicao):
        posicao= posicao - 1
        if posicao >= cls.id | posicao < 0:
            print("Posição invalida")
            return
        del cls.estoques[posicao]
    @classmethod
    def quantidade(cls, mensagem):
        quantidade = int(input(mensagem))
        if quantidade<= 0:
            return cls.quantidade()
        return quantidade
    @classmethod  
    def add_peso_volume(cls, newproduto, mensagem):
        test = False
        while test == False:
            vari= int(input(mensagem))
            test= newproduto.addpeso_volume(vari)
    @classmethod  
    def add_p_v(cls, newproduto):
        test = False
        while test == False:
            unidade = input ("Informe a unidade de medida (ex: ml ou g) que sera utilizada: ")
            vari= int(input("Peso/volume do produto: "))
            test= newproduto.addvolume(vari, unidade)
        
    @classmethod
    def add_alimento(cls, nome, marca, data_venc):
        quantidade= cls.quantidade("Quantidade adicionada: ")
        preco = cls.quantidade("Preco do produto: ")
        newproduto = Alimentos(nome, marca, data_venc, 0, quantidade, preco)
        cls.add_peso_volume(newproduto, "Peso em gramas do produto: ")       
        cls.addproduct(newproduto)

    @classmethod
    def add_bebida(cls, nome, marca, data_venc):
        quantidade= cls.quantidade("Quantidade adicionada: ")
        preco = cls.quantidade("Preco do produto: ")
        newproduto = Bebidas(nome, marca, data_venc, 0, quantidade, preco)
        cls.add_peso_volume(newproduto, "Volume em ml do produto: ")
        cls.addproduct(newproduto)

    @classmethod
    def add_higiene(cls, nome, marca, data_venc):
        quantidade= cls.quantidade("Quantidade adicionada: ")
        preco = cls.quantidade("Preco do produto: ")
        newproduto = Higiene(nome, marca, data_venc, 0, quantidade, preco)
        test = False
        cls.add_p_v(newproduto)
        cls.addproduct(newproduto)

    @classmethod
    def search(cls):
        posi= int(input("Informe a posição do produto no estoque: "))
        posi= posi-1
        if(posi >= cls.id | posi< 0):
            return cls.search
        return posi

    @classmethod
    def altera_peso_volume(cls, produto):
        str = produto.tipo_produto()
        print(str)
        if str == "Alimento":
           cls.add_peso_volume(produto, "Peso em gramas do produto: ")
        elif str == "Bebida":
            cls.add_peso_volume(produto, "Volume em ml do produto: ")
        elif  str == "Higiene":
            cls.add_p_v(produto)
        else:
            print("errooo")
    @classmethod
    def altera_dados(cls, tipo):
        prateleira= list(cls.estoques.values())
        produto= int(cls.search())
        if tipo == 1:
            nome = input("Novo nome do empregado: ")
            prateleira[produto].nome(nome)
        elif tipo ==2:
            marca = input("Nova marca do produto: ")
            prateleira[produto].marca(marca)
        elif tipo==3:
            preco = cls.quantidade("Preco do produto: ")
            prateleira[produto].preco(preco)
        elif tipo==4:
            quantidade= cls.quantidade("Quantidade adicionada: ")
            prateleira[produto].quantitade(quantidade)
        elif tipo == 5:
            cls.altera_peso_volume(prateleira[produto])
    @classmethod
    def select_tipo(cls):
        print("Informe o tipo de produto :\n1-Alimento\n2- Bebidas\n3- Higiene\n")
        choice = int(input())
        if choice == 1:
            PrintInfo.print_tipos(cls.estoques.values(), "Alimento")
        elif choice == 2:
            PrintInfo.print_tipos(cls.estoques.values(), "Bebida")
        elif choice == 3:
            PrintInfo.print_tipos(cls.estoques.values(), "Higiene")
    @classmethod
    def print_infos(cls,choice):
        if choice == 1:
            PrintInfo.printestoque(cls.estoques.values())
        elif choice == 2:
            PrintInfo.print_marca(cls.estoques.values())
        elif choice == 3:
            PrintInfo.print_data(cls.estoques.values())
        elif choice ==4:
            cls.select_tipo()
    @classmethod
    def print_venc(cls):
        PrintInfo.print_venc(cls.estoques.values())
            