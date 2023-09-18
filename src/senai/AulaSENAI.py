import os
import SENAI.POO as POO
'''
Autor: João Victor Martins Deamo
Date: 18/09/2023
Time: 08:19
IDE: Visual Studio Code
Session Duration: 08:19 - 11:10
Subject: Python
Version: 1.0
Senai - Desenvolvimento de Sistemas
'''
def clear_screen():
    os.system('cls')
def welcome_message():
    print("Seja bem-vindo(a) ao App Senai!")
# Função iniciar
def iniciar():
    try:
        clear_screen()
        welcome_message()
        print("Iniciando...")
        menu()
        poo()
    except Exception as e:
        print("Erro: ", e)
# Função atributos   
def atributos(nome, idade):
    try:
        nome = "João Victor"
        idade = 19
        # usando o f-string para concatenar variáveis com strings
        print(f"Nome do aluno: {nome}.\nIdade: {idade}.")   
        '''
        Usando o format para concatenar variáveis com strings
        print("Nome do aluno: {}.\nIdade: {}.".format(nome, idade))
        '''
    except Exception as e:
        print("Erro: ", e)

# Função que recebe um nome como parâmetro e retorna o nome
def saudacaonome(nome):
    try:
        print(f"Olá, {nome}!")
        return nome
    except Exception as e:
        print("Erro: ", e)
def frases():
    try:
        frases = "O importante não é vencer todos os dias, mas lutar sempre."
        quantidade = len(frases)
        print(f"A frase tem {quantidade} caracteres.")
        quantidadeLetras = frases.count("a")
        print(f"A letra 'a' aparece {quantidadeLetras} vezes.")
    except Exception as e:
        print("Erro: ", e)

def lista():
    try:
        frutas = ["maçã", "banana", "laranja", "melancia"]
        print(f"Lista de frutas: {frutas}")
        frutas[:] = "abacaxi", "abacate", "acerola", "amora"
        frutas.append("morango")
        print(f"Lista de frutas modificada: {frutas}")
        # print(f"Primeira fruta da sacola: {frutas[0]}")
        # Manipulando listas
        # Substituindo os valores da lista frutas [0], [1], [2], [3]
        # print(f"Última fruta da sacola: {frutas[-1]}")
    except Exception as e:
        print("Erro: ", e)

def dicionários():
    try:
        coordenadas = (10, 20)
        x = coordenadas[0]
        y = coordenadas[1]
        print(f"Coordenadas: {coordenadas}")
        print(f"Coordenadas x, y: {x}, {y}.")
        ''' Desempacotamento de tuplas
        x, y = coordenadas
        print(f"Coordenada x: {x}")
        print(f"Coordenada y: {y}")
        '''
        pessoa = {"nome": "João Victor", "idade": 19, "altura": 1.84, "peso": 84.3}
        # print(f"Pessoa: {pessoa}")
        # Percorrendo o dicionário
        for chave, valor in pessoa.items():
            print(f"{chave}: {valor}")
        # Acessando os valores do dicionário
        nomePessoa, idadePessoa, alturaPessoa, pesoPessoa = pessoa["nome"], pessoa["idade"], pessoa["altura"], pessoa["peso"]
        # print(f"Dados da pessoa: {nomePessoa}, idade: {idadePessoa}, altura: {alturaPessoa}, peso: {pesoPessoa}")

        nomePessoa = "Carlinhos"
        idadePessoa = 20
        alturaPessoa = 1.70
        pesoPessoa = 70.0
        pessoa["profissão"] = "Desenvolvedor"
        del pessoa["peso"]
        # Imprimindo as variáveis, que receberam os valores do dicionário
        print(f"Dados da pessoa: {nomePessoa}, idade: {idadePessoa}, altura: {alturaPessoa}, peso: {pesoPessoa}, profissão: {pessoa['profissão']}")

        # Imprimindo os valores do dicionário
        print(f"Nome da pessoa: {pessoa['nome']}, idade: {pessoa['idade']}, altura: {pessoa['altura']}, profissão: {pessoa['profissão']}")
        '''
    Imprimindo os valores do dicionário
    print(f"Valores do dicionário: {pessoa.values()}")
    Imprimindo as chaves do dicionário
    print(f"Chaves do dicionário: {pessoa.keys()}")
    '''
    except Exception as e:
        print("Erro: ", e)
# Função para chamar as outras funções
def menu():
    clear_screen()
    welcome_message()
    try:
        atributos("João Victor", 19)
        saudacaonome("João Victor")
        frases()
        lista()
        dicionários()

    except Exception as e:
        print("Erro: ", e) 

def dadosObjetos():
    try:
        nome, idade, altura, peso, marca, modelo, ano, cor = POO.objetos(None, None)
        if nome is not None and marca is not None:
            print(f"Nome: {nome}, idade: {idade}, altura: {altura}, peso: {peso}")
            print(f"Marca: {marca}, modelo: {modelo}, ano: {ano}, cor: {cor}")

        else:
            print("Não foi possível criar as instâncias das classes.")
        '''
        pessoa = POO.classes("XIS", 35, 1.61, 45.3)
        carro = POO.classes("Fiat", "Uno", 2010, "Preto")
        print(f"Nome: {pessoa.nome}, idade: {pessoa.idade}, altura: {pessoa.altura}, peso: {pessoa.peso}")
        print(f"Marca: {carro.marca}, modelo: {carro.modelo}, ano: {carro.ano}, cor: {carro.cor}")
        '''
    except Exception as e:
        print("Erro: ", e)

# Função principal POO
def poo():
    try:
        dadosObjetos()
    except Exception as e:
        print("Erro: ", e)


# Função main
def main():
    iniciar()
if __name__ == "__main__":
    main()