# Bibliotecas
import os # Para fazer o clear
import msvcrt # Para conseguir o input de uma tecla sem precisar apertar enter
import random # Gerar numeros aleatorios


# Declaração das filas
class Fila:
    def __init__(self):
        self.fim = -1
        # Criando uma 'array' / tecnicamente é uma lista mas serve
        self.numeros = [0]
        # Limpando todos os espaços da lista e deixando vazia
        self.numeros.clear()

    def pushFila(self):
        # Função para inserção de um elemento na fila
        if self.fim == 4:
            print('Fila cheia!')
            # pausando tela para poder ler
            pause()
        else:
            print('Coloque um número para inserir na fila:', end=' ')
            num = checaNumero(input())
            self.fim += 1
            self.numeros.append(int(num))
            print('Número inserido:', num)
            pause()
    def popFila(self):
        # Função para remover um elemento da fila
        if len(self.numeros) == 0:
            print('Fila vazia!')
            pause()
        else:
            # Variavel de confirmacao
            remova = False
            print('Deseja remover último elemento?')
            print('Aperte <s> para confirmar ação')
            opc = msvcrt.getwch()
            if opc == 's':
                remova = True
            if remova:
                self.numeros.pop(0)
                print('Elemento removido.')
            else:
                print('Elemento não será removido.')
            pause()
    def verFila(self):
        # Função para ver elemento da fila
        if len(self.numeros) == 0:
            print('Fila vazia.')
            pause()
        else:
            # x é uma variável auxiliar
            x = 1
            for i in self.numeros:
                print(f'Elemento {x}: {i}')
                x += 1
            pause()
    
    def gerarFila(self):
        # Função para gerar números aleatórios na fila
        # J serve para saber quantos elementos foram gerados
        j = 5 - len(self.numeros)
        # Fazendo uma repeticao que comeca na quantidade de elementos que ja tem e vai ate 5, que é o máximo de numero da fila
        for i in range(len(self.numeros), 5, 1):
            self.numeros.append(random.randint(1, 999))
        print(f'{j} elementos gerados.')
        pause()


# Declaração das pilhas
class Pilha:
    def __init__(self):
        self.topo = -1
        # Criando uma 'array' / tecnicamente é uma lista mas serve
        self.numeros = [0]
        # Limpando todos os espaços da nova lista e deixando vazia
        self.numeros.clear()

    def pushPilha(self):
        # Função para inserção de um elemento na pilha
        if self.topo == 4:
            print('Pilha cheia!')
            # Para pausar a tela
            pause()
        else:
            print('Coloque um número para inserir na pilha:', end=' ')
            num = checaNumero(input())
            self.topo += 1
            self.numeros.append(int(num))
            print(f'Número inserido: {num}')
            pause()

    def verPilha(self):
        # Função para ver a pilha
        # Testando para ver caso a pilha esteja vazia
        if len(self.numeros) == 0:
            print('Pilha vazia.')
        else:
            # x é uma variável auxiliar para numerar os elementos
            x = 1
            for i in self.numeros:
                print(f'Elemento {x}: {i}')
                x += 1
        pause()

    def popPilha(self):
        # Função para remover um elemento da pilha
        if len(self.numeros) == 0:
            print('Pilha vazia!')
            # Para pausar a tela
            pause()
        else:
            # Variavel para confirmar ação
            remova = False
            # Menu para confirmar ação
            print('Deseja remover último elemento?')
            print('Aperte <s> para confirmar ação')
            opc = msvcrt.getwch()
            if opc == 's':
                remova = True
            if remova:
                self.numeros.pop(self.topo)
                self.topo -= 1
                print('Elemento removido.')
            else:
                print('Elemento não será removido.')
            pause()

    def gerarPilha(self):
        # Função para gerar números aleatórios na fila
        # J serve para saber quantos elementos foram gerados
        j = 5 - len(self.numeros)
        # Colocando o topo
        self.topo = j - 1
        # Fazendo uma repeticao que comeca na quantidade de elementos que ja tem e vai ate 5, que é o máximo de numero da fila
        for i in range(len(self.numeros), 5, 1):
            self.numeros.append(random.randint(1, 999))
        print(f'{j} elementos gerados.')
        pause()


# Coisas da superfila
class Superfila:
    def __init__(self):
        self.fim = -1
        # Criando uma 'array' / tecnicamente é uma lista mas serve
        self.numeros = [0]
        # Limpando todos os espaços da lista e deixando vazia
        self.numeros.clear()

    def limparSuperFila(self):
        # Limpando a super fila
        self.numeros.clear()
  
    def verFila(self):
        # Função para ver elemento da fila
        if len(self.numeros) == 0:
            print('Fila vazia.')
        else:
            # x é uma variável auxiliar
            x = 1
            for i in self.numeros:
                print(f'Elemento {x}: {i}')
                x += 1
        pause()
    
    def gerarFila(self):
        # Colocando a pilha dentro da fila
        # Criando uma copia da pilha
        self.numeros = pilha.numeros.copy()
        # Invertendo lista da pilha para colocar sempre os ultimos valores da pilha primeiro
        self.numeros.reverse()
        # Inserindo fila na super fila
        self.numeros.extend(fila.numeros)
    

# Menu para mexer na pilha
def menu_pilha():
    repeat = True
    while repeat:
        clear()
        print('Escolha uma opção:')
        print('<1> Colocar elemento na pilha')
        print('<2> Remover elemento na pilha')
        print('<3> Ver a pilha')
        print('<4> Preencher com números aleatórios')
        print('<5> Sair')
        escolha = msvcrt.getwch()
        match escolha:
            case '1':
                clear()
                pilha.pushPilha()
            case '2':
                clear()
                pilha.popPilha()
            case '3':
                clear()
                pilha.verPilha()
            case '4':
                clear()
                pilha.gerarPilha()
            case '5':
                sair = False # Variável para controlar se o usuário realmente deseja sair do programa
                clear()
                print('Deseja sair do menu de pilha?\nAperte <s> para confirmar')
                opc = msvcrt.getwch()
                if opc == 's':
                    repeat = False


# Menu para mexer na fila
def menu_fila():
    repeat = True
    while repeat:
        clear()
        print('Escolha uma opção:')
        print('<1> Colocar elemento na fila')
        print('<2> Remover elemento na fila')
        print('<3> Ver a fila')
        print('<4> Preencher com números aleatórios')
        print('<5> Sair')
        escolha = msvcrt.getwch()
        match escolha:
            case '1':
                clear()
                fila.pushFila()
            case '2':
                clear()
                fila.popFila()
            case '3':
                clear()
                fila.verFila()
            case '4':
                clear()
                fila.gerarFila()
            case '5':
                sair = False # Variável para controlar se o usuário realmente deseja sair do programa
                clear()
                print('Deseja sair do menu de fila?\nAperte <s> para confirmar')
                opc = msvcrt.getwch()
                if opc == 's':
                    repeat = False


# Menu para mexer nas opções
def menu():
    nunca_gerado = True # Variavel de controle das opções de superfila
    repeat = True
    while repeat:
        clear()
        print('Escolha uma opção:')
        print('<1> Menu das pilhas')
        print('<2> Menu das filas')
        print('<3> Gerar superfila')
        print('<4> Ver superfila')
        print('<5> Sair')
        escolha = msvcrt.getwch()
        match escolha:
            case '1':
                clear()
                menu_pilha()
            case '2':
                clear()
                menu_fila()
            case '3':
                clear()
                if len(pilha.numeros) == 0 and len(fila.numeros) == 0: # CASO NAO TENHA NADA NA FILA NEM NA PILHA
                    print('Pilha e Filas com elementos vazios!')
                    pause()
                elif nunca_gerado:
                    superfila.gerarFila()
                    print('Super fila gerada!')
                    nunca_gerado = False
                    pause()
                else:
                    superfila.limparSuperFila()
                    superfila.gerarFila()
                    print('Nova super fila gerada!')
                    pause()
            case '4':
                clear()
                if nunca_gerado:
                    print('Você não gerou uma Super Fila ainda!')
                    pause()
                else:
                    superfila.verFila()
            case '5':
                sair = False # Variável para controlar se o usuário realmente deseja sair do programa
                clear()
                print('Deseja sair do programa?\nAperte <s> para confirmar')
                opc = msvcrt.getwch()
                if opc == 's':
                    repeat = False


# MACROS
# clear = para limpar o terminal de mensagens
clear = lambda: os.system('cls')
# pause = auto explicatorio...
def pause():
    print('\nPressione qualquer botão...')
    msvcrt.getch()
# método para não deixar caracteres serem inseridos
def checaNumero(x):
    if x.isdecimal():
        # Caso seja um número: retorna o número
        return x
    else:
        # Caso não digite um número
        # Repetir até conseguir um número
        while True:
            clear()
            print('Por favor, digite um número válido:', end= ' ')
            x = input()
            if x.isdecimal():
                return x
    

# Programa principal
if __name__ == '__main__':
    # Settando uma seed pra gerar numeros aleatorios
    random.seed()
    # Limpando tela ao iniciar
    clear()
    # Instanciando pilha
    pilha = Pilha()
    fila = Fila()
    superfila = Superfila()
    # Iniciando menu
    menu()