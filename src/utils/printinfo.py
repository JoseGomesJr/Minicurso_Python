from datetime import datetime

class PrintInfo:
    @classmethod
    def print_tipos(cls,estoques, mensagem):
        cont= 1
        for produtos in estoques:
            if produtos.tipo_produto() == mensagem:
                print("Posição no estoque ["+ str(cont) + "]\nTipo de produto ", produtos.tipo_produto())
                print(produtos)
            cont= cont+1
    @classmethod
    def print_marca(cls,estoques, mensagem):
        cont= 1
        for produtos in estoques:
            if produtos.marca() == mensagem:
                print("Posição no estoque ["+ str(cont) + "]\nTipo de produto ", produtos.tipo_produto())
                print(produtos)
            cont= cont+1
    @classmethod       
    def teste_data(cls, date_1, date_2):
        quantidade_dias = abs((date_1 - date_2).days)
        if quantidade_dias <= 30:
            return True
        else:
            return False
    @classmethod
    def print_data(cls, estoques):
        cont= 1
        date_1= datetime.now()
        for produtos in estoques:
            date_2= produtos.data_now()
            teste= cls.teste_data(date_1, date_2)
            if teste == True:
                print("Posição no estoque ["+ str(cont) + "]\nTipo de produto ", produtos.tipo_produto())
                print(produtos)
            cont= cont+1
    @classmethod
    def printestoque(cls, estoques):
        cont= 1
        for produtos in estoques:
            print("Posição no estoque ["+ str(cont) + "]\nTipo de produto ", produtos.tipo_produto())
            print(produtos)
            cont= cont+1
    @classmethod
    def print_venc(cls, estoques):
        cont= 1
        date_1= datetime.now()
        print("Os produtos com vencimentos com 30 dias ou menos")
        for produtos in estoques:
            date_2= produtos.data_venc()
            teste= cls.teste_data(date_2, date_1)
            if teste == True:
                print("Posição no estoque ["+ str(cont) + "]\nTipo de produto ", produtos.tipo_produto())
                print(produtos)
            cont= cont+1