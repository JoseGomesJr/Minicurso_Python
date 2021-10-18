from src import Estoque
from src import PrintMenu

class Menu:
    @classmethod
    def tipos_de_produto(cls, nome_, marca, data_venc):
        print("Informe o tipo de produto que vai ser adicionado:\n1-Alimento\n2- Bebidas\n3- Higiene\n")
        choice=''
        choice = PrintMenu.validChoice(choice, 3, "Informe a opção")
        if choice == 1:
            Estoque.add_alimento(nome_, marca, data_venc)
        elif choice == 2:
            Estoque.add_bebida(nome_, marca, data_venc)
        else:
            Estoque.add_higiene(nome_, marca, data_venc)
    
    @classmethod
    def Add(cls):
        choice=""
        nome = input("Insira o nome do produto: ")
        marca = input("Insira o nome da marca: ")
        data_venc = PrintMenu.valdDateChoice(choice, 6, "Insira a data de vencimento: ")
        cls.tipos_de_produto(nome, marca, data_venc)

    @classmethod
    def remove(cls):
        posicao= int(input("Informe o Numero da Posição do produto: "))
        Estoque.remove(posicao)
    @classmethod
    def print_info(cls):
        choice = 0
        choice = int(PrintMenu.validChoice(choice, 5, PrintMenu.print_inf))
        Estoque.print_infos(choice)
    @classmethod
    def print_venc(cls):
       Estoque.print_venc()
    
    @staticmethod
    def quit():
        print("Até mais :)")
    @classmethod
    def option(cls, choice):
        {
        1: cls.Add,
        2: cls.remove,
        3: cls.mudar,
        4: cls.print_info,
        5: cls.print_venc,
        6: cls.quit,
        }.get(choice)()
    @classmethod
    def mudar(cls):
        choice = 0
        choice = int(PrintMenu.validChoice(choice, 5, PrintMenu.mudar))
        Estoque.altera_dados(choice)
    @classmethod
    def menu(cls):
        choice = ""
        while choice != 6:
            choice = ""
            choice = PrintMenu.validChoice(choice, 6, PrintMenu.menu)
            cls.option(choice)

if __name__ == "__main__":
    Menu.menu()