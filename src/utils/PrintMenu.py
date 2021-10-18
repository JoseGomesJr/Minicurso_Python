from datetime import datetime
import textwrap

class PrintMenu:
    menu = textwrap.dedent("""\
                                ==========================================
                                O que deseja fazer, hoje?
                                    [1] - Adicionar produto
                                    [2] - Remover produto
                                    [3] - Altera informações de produto
                                    [4] - Relatorio de Informações
                                    [5] - Relatorio de Validade
                                    [6] - Sair
                                    \n""")
    mudar = textwrap.dedent("""\
                                ==========================================
                                O que deseja mudar?
                                    [1] - Alterar nome
                                    [2] - Alterar marca
                                    [3] - Alterar preço
                                    [4] - Altera quantidade
                                    [5] - Alterar Peso ou Volume
                                    \n""")
    print_inf = textwrap.dedent("""\
                                ==========================================
                                Quais produtos deseja ver?
                                    [1] - Todos os produtos
                                    [2] - Da mesma marca
                                    [3] - Adicionados no ultimo mes
                                    [4] - Mesmo tipo
                                    [5] - Sair
                                    \n""")
    @staticmethod
    def errorMessage():
        print("Opção inválida")
    
    @staticmethod
    def validIntChoice(choice):
        try:
            choice = int(choice)
            return choice
        except:
            pass
    @staticmethod
    def valDateChoice(choice):
        try:
            newDate = datetime.strptime(choice, '%d-%m-%Y').date()
            correctDate = True
        except ValueError:
            correctDate = False
        return correctDate
    @staticmethod
    def validChoice(choice, options, message):
        while choice not in list(range(1, options+1)):
                print(message, end = "")
                choice = input()
                choice = PrintMenu.validIntChoice(choice)
                if choice not in list(range(1, options+1)):
                    PrintMenu.errorMessage()
        return choice
    @staticmethod
    def valdDateChoice(choice, options, message):
        
        test= None
        while test != True:
            print(message, end = "")
            choice = input()
            test = PrintMenu.valDateChoice(choice)
        return choice
    def isInstance(employee, type):
        if isinstance(employee, type):
            return True
        return print("Operação não permitida")
        
    def produtos(estoque):
        for produtos in estoque:
            print(produtos)
        print("\n", end="")