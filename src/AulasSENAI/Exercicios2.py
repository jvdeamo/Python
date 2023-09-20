import os
import time

'''
Autor: João Victor Martins Deamo
Date: 18/09/2023
Time: 08:52
IDE: Visual Studio Code
Session Duration: 08:52 - 11:42
Subject: Python
Version: 1.0
Senai - Desenvolvimento de Sistemas

Exercício 1: Calculadora Avançada

Crie uma função chamada calculadora_avancada que permita ao usuário escolher entre várias operações matemáticas, como adição, subtração, multiplicação e divisão. A função deve receber dois números e a operação desejada como entrada e retornar o resultado da operação.

Exercício 2: Média de Notas

Escreva um programa que solicite ao usuário que digite várias notas e, em seguida, calcule a média dessas notas. O programa deve continuar pedindo notas até que o usuário decida parar. Implemente isso usando uma função chamada calcular_media_notas.

Exercício 3: Números Primos

Crie uma função chamada verificar_numero_primo que recebe um número inteiro como entrada e verifica se ele é um número primo ou não. A função deve retornar True se o número for primo e False caso contrário.

Exercício 4: Gerador de Sequência de Fibonacci

Implemente uma função chamada gerar_fibonacci que recebe um número inteiro n como entrada e gera os primeiros n termos da sequência de Fibonacci. A sequência de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos dois termos anteriores.

Exercício 5: Contagem de Palavras

Crie uma função chamada contar_palavras que recebe uma string como entrada e conta quantas palavras existem na string. Considere que as palavras são separadas por espaços em branco.
'''


def clear_screen():
    os.system('cls')


def welcome_message():
    print("Seja bem-vindo(a) ao App Senai!")
# Função iniciar


def iniciar():
    try:
        clear_screen()
        print("Iniciando...")
        welcome_message()
        menuSenai()
    except Exception as e:
        print("Erro: ", e)


def menuSenai():
    try:
        print("1 - Cálculos")
        print("2 - Sair")

        opcao = int(input("Digite a opção desejada: "))
        clear_screen()
        if opcao == 1:
            calculos = menuCalculos()
            if calculos is None:
                return False
        elif opcao == 2:
            print("Saindo...")
            time.sleep(1)
            clear_screen()
            print("Obrigado por usar o App Senai!")
            return False
        else:
            print("Opção inválida!")
            time.sleep(1)
            clear_screen()
        return True
    except Exception as e:
        print("Erro: ", e)


def menuCalculos():
    try:
        print("Calculadora - Sistema SENAI")
        print("1 - Calculadora")
        print("2 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        clear_screen()
        if opcao == 1:
            calculadora = exercicios()
            if calculadora is None:
                return False
        elif opcao == 2:
            print("Saindo...")
            time.sleep(1)
            clear_screen()
            return False
        else:
            print("Opção inválida!")
            time.sleep(1)
            clear_screen()
        return True
    except Exception as e:
        print("Erro: ", e)


def exercicios():
    # Exercício 1
    def calculadoraAvancada():
        class Calculadora:
            def calculadoraAdicao(self, num1, num2):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 + num2
                clear_screen()
                print(f"[{num1} + {num2}] = {resultado}")
                return resultado

            def calculadoraSubtracao(self, num1, num2):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 - num2
                clear_screen()
                print(f"[{num1} - {num2}] = {resultado}")
                return resultado

            def calculadoraMultiplicacao(self, num1, num2):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = float(num1 * num2)
                clear_screen()
                print(f"[{num1} * {num2}] = {resultado}")
                return resultado

            def calculadoraDivisao(self, num1, num2):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = float(num1 / num2)
                clear_screen()
                print(f"[{num1} / {num2}] = {resultado}")
                return resultado
        calculadora = Calculadora()
        print("Calculadora Avançada - Sistema SENAI")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        clear_screen()
        if opcao == 1:
            calculadora.calculadoraAdicao(None, None)
            calculadoraAvancada()
        elif opcao == 2:
            calculadora.calculadoraSubtracao(None, None)
            calculadoraAvancada()
        elif opcao == 3:
            calculadora.calculadoraMultiplicacao(None, None)
            calculadoraAvancada()
        elif opcao == 4:
            calculadora.calculadoraDivisao(None, None)
            calculadoraAvancada()
        elif opcao == 5:
            print("Saindo...")
            time.sleep(1)
            clear_screen()
            return False
        else:
            print("Opção inválida!")
            time.sleep(1)
            clear_screen()
            calculadoraAvancada()
        return Calculadora()
        calculadoraAvancada()
    # Exercício Lenon

    def calculadoraLemon():
        class Calculadora:
            def calculadoraAdicao(self, num1, num2):
                resultado = float(num1 + num2)
                clear_screen()
                print(f"[{num1} + {num2}] = {resultado}")
                return resultado

            def calculadoraSubtracao(self, num1, num2):
                resultado = float(num1 - num2)
                print(f"[{num1} - {num2}] = {resultado}")
                return resultado

            def calculadoraMultiplicacao(self, num1, num2):
                resultado = float(num1 * num2)
                clear_screen()
                print(f"[{num1} * {num2}] = {resultado}")
                return resultado

            def calculadoraDivisao(self, num1, num2):
                resultado = float(num1 / num2)
                clear_screen()
                print(f"[{num1} / {num2}] = {resultado}")
                return resultado
        calculadora = Calculadora()
        print("Calculadora Lemon - Sistema SENAI")
        # loop while
        while True:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação desejada: ")
            num2 = float(input("Digite o segundo número: "))

            if operacao == "+":
                calculadora.calculadoraAdicao(num1, num2)
            elif operacao == "-":
                calculadora.calculadoraSubtracao(num1, num2)
            elif operacao == "*":
                calculadora.calculadoraMultiplicacao(num1, num2)
            elif operacao == "/":
                calculadora.calculadoraDivisao(num1, num2)
            else:
                print("Operação inválida!")
                time.sleep(1)
                clear_screen()
                calculadoraLemon()
                return Calculadora()
            sair = input("Deseja sair? (s/n): ")
            if sair == "s":
                print("Saindo...")
                time.sleep(1)
                clear_screen()
                break
            elif sair == "n":
                print("Continuando...")
                time.sleep(1)
                clear_screen()
                calculadoraLemon()
                break
            else:
                print("Opção inválida!")
                time.sleep(1)
                clear_screen()
                calculadoraLemon()
        calculadoraLemon()
    # Exercício 2

    def calculadoraNotas():
        try:
            def menu():
                try:
                    while True:
                        print("Calculadora Notas - Sistema SENAI")
                        print("1 - Notas")
                        print("2 - Sair")
                        opcao = int(input("Digite a opção desejada: "))
                        clear_screen()
                        if opcao == 1:
                            notas = menu_notas()
                            if notas is None:
                                return False
                        elif opcao == 2:
                            print("Saindo...")
                            time.sleep(1)
                            clear_screen()
                            return False
                        else:
                            print("Opção inválida!")
                            time.sleep(1)
                            clear_screen()
                        return True
                except Exception as e:
                    print("Erro: ", e)

            def menu_notas():
                try:
                    notas = []
                    while True:
                        print("Módulo Notas - Sistema SENAI")
                        print("1 - Inserir notas")
                        print("2 - Calcular média das notas")
                        print("3 - Sair")
                        opcao = int(input("Digite a opção desejada: "))
                        clear_screen()
                        if opcao == 1:
                            for i in range(5):
                                try:
                                    nota = float(
                                        input(f"Digite a {i + 1}ª nota: "))
                                    notas.append(nota)
                                except ValueError as e:
                                    print("Erro: ", e)
                            clear_screen()
                        elif opcao == 2:
                            if not notas:
                                print("Você precisa inserir notas primeiro.")
                            else:
                                calcular_media_notas(notas)
                        elif opcao == 3:
                            print("Saindo...")
                            time.sleep(1)
                            clear_screen()
                            return None
                        else:
                            print("Opção inválida!")
                            time.sleep(1)
                            clear_screen()
                except Exception as e:
                    print("Erro: ", e)

            def calcular_media_notas(notas):
                try:
                    media = (sum(notas) / len(notas))
                    print(f"Média: {media}")
                    sair = input("Deseja sair? (s/n): ")
                    if sair == "s":
                        print("Saindo...")
                        time.sleep(1)
                        clear_screen()
                        return False
                    elif sair == "n":
                        print("Continuando...")
                        time.sleep(1)
                        clear_screen()
                    else:
                        print("Opção inválida!")
                        time.sleep(1)
                        clear_screen()
                except Exception as e:
                    print("Erro: ", e)

            def escola():
                try:
                    while True:
                        continuar = menu()
                        if not continuar:
                            break
                except Exception as e:
                    print("Erro: ", e)
        except Exception as e:
            print("Erro: ", e)
        escola()
        calculadoraNotas()

    # Exercício 3
    def calculadoraNumeroPrimo():
        try:
            def menu():
                print("Calculadora Número Primo - Sistema SENAI")
                print("1 - Verificar número primo")
                print("2 - Sair")
                opcao = int(input("Digite a opção desejada: "))
                clear_screen()
                if opcao == 1:
                    verificar_numero_primo()
                elif opcao == 2:
                    print("Saindo...")
                    time.sleep(1)
                    clear_screen()
                    return False
                else:
                    print("Opção inválida!")
                    time.sleep(1)
                    clear_screen()
                return True
            menu()

            def verificar_numero_primo(num):
                try:
                    num = int(input("Digite um número: "))
                    try:
                        num = int(num)
                    except ValueError:
                        print("Digite um número inteiro!")
                    if num > 1:
                        for i in range(2, num):
                            if (num % i) == 0:
                                print(f"{num} não é um número primo")
                                break
                        else:
                            print(f"{num} é um número primo")
                    else:
                        print(f"{num} não é um número primo")
                    sair = input("Deseja sair? (s/n): ")
                    if sair == "s":
                        print("Saindo...")
                        time.sleep(1)
                        clear_screen()
                        return False
                    elif sair == "n":
                        print("Continuando...")
                        time.sleep(1)
                        clear_screen()
                        menu()
                    else:
                        print("Opção inválida!")
                        time.sleep(1)
                        clear_screen()
                except Exception as e:
                    print("Erro: ", e)
        except Exception as e:
            print("Erro: ", e)
        calculadoraNumeroPrimo()

    # Exercício 4
    def calculadoraFibonacci():
        print("Calculadora Fibonacci - Sistema SENAI")

    def calculadoraContagemPalavras():
        print("Calculadora Contagem de Palavras - Sistema SENAI")

    def menuCalculadora():
        try:
            print("Calculadora - Sistema SENAI")
            print("1 - Calculadora Avançada")
            print("2 - Calculadora Notas")
            print("3 - Calculadora número primo")
            print("4 - Calculadora Fibonacci")
            print("5 - Calculadora Contagem de Palavras")
            print("6 - Sair")
            print("26 - Calculadora Lemon")
            opcao = int(input("Digite a opção desejada: "))
            clear_screen()
            if opcao == 1:
                calculadoraAvancada()
            elif opcao == 2:
                calculadoraNotas()
            elif opcao == 3:
                calculadoraNumeroPrimo()
            elif opcao == 4:
                calculadoraFibonacci()
            elif opcao == 5:
                calculadoraContagemPalavras()
            elif opcao == 6:
                print("Saindo...")
                time.sleep(1)
                clear_screen()
                return False
            elif opcao == 26:
                calculadoraLemon()
            else:
                print("Opção inválida!")
                time.sleep(1)
                clear_screen()
            return True
        except Exception as e:
            print("Erro: ", e)
    menuCalculadora()

# Função main


def main():
    try:
        iniciar()
    except Exception as e:
        print("Erro: ", e)


# Inicialização do programa
if __name__ == "__main__":
    main()
