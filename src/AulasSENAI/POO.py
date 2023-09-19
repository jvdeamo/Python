def classes():
    try:
        class Pessoa:
            def __init__(self, nome, idade, altura, peso):
                self.nome = nome
                self.idade = idade
                self.altura = altura
                self.peso = peso
            def __str__(self):
                return f"Nome: {self.nome}, idade: {self.idade}, altura: {self.altura}, peso: {self.peso}"
    
        class Carro:
            def __init__(self, marca, modelo, ano, cor):
                self.marca = marca
                self.modelo = modelo
                self.ano = ano
                self.cor = cor
            def __str__(self):
                return f"Marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}, cor: {self.cor}"
        
        # Criando as instâncias das classes
        pessoa = Pessoa("João Victor", 19, 1.84, 84.3)
        carro = Carro("Fiat", "Uno", 2010, "Preto")
        return pessoa, carro
    except Exception as e:
        print("Erro: ", e)
        return None, None

# Criar uma função para obter os valores das instâncias das classes
def objetos(pessoa, carro):
    try:
        # Obtendo as instâncias das classes
        pessoa, carro = classes()
        return pessoa.nome, pessoa.idade, pessoa.altura, pessoa.peso, carro.marca, carro.modelo, carro.ano, carro.cor
    except Exception as e:
        print("Erro: ", e)


def main():
    try:
        classes()
    except Exception as e:
        print("Erro: ", e)