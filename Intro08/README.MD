

# Classe, método e Instancia

## Metodo
- Uma funcao dentro da classe que faz alguma acao estabelecida
```
# Usando o método da classe

Func1.listFunc()
```
## Instancia
- Criacao de alguma variavel que utiliza a classe
```
# A lista lst_num é um objeto, uma instância da classe lista em Python

type(lst_num)
```
## Atributo
- Quando chamamos alguma caracteristica especifica da nossa Classe
```
# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe

Estudante1.idade
```
## Classes

Em Programação Orientada a Objetos (POO), uma classe é uma estrutura que descreve um objeto, especificando os atributos e comportamentos que o objeto deve ter. Uma classe é uma espécie de modelo que define as características e ações que um objeto deve possuir.

As classes são usadas para criar objetos, que são instâncias da classe. Cada objeto criado a partir da mesma classe terá os mesmos atributos e comportamentos.

Para criar uma classe em Python, utiliza-se a palavra reservada class.

O nome da classe segue a mesma convenção de nomes para criação de funções e variáveis em Python, mas normalmente se usa a primeira letra maiúscula em cada palavra no nome da classe.


```
# Criando uma classe chamada Livro

class Livro():

    # Este método vai inicializar cada objeto criado a partir desta classe

    # O nome deste método é __init__

    # (self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)

    def __init__(self):

        # Atributos são propriedades

        self.titulo = 'Sapiens - Uma Breve História da Humanidade'

        self.isbn = 9988888

        print("Construtor chamado para criar um objeto desta classe.")

    # Métodos são funções que executam ações nos objetos da classe

    def imprime(self):

        print("Foi criado o livro %s com ISBN %d" %(self.titulo, self.isbn))
```

Def '''__init__''(self) é construtor 
	Para Inicializar os atributos da classe

Em Python, a palavra reservada self é uma referência ao objeto atual da classe. Quando um objeto é criado a partir de uma classe, self é utilizado para se referir a esse objeto específico

### Criando uma instancia de classe Livro
```
# Criando uma instância da classe Livro

Livro1 = Livro()
```

Aqui nesse caso, o Livro1 terá os "atributos" da classe "Livro"

### Colocando parametros no método construtor
```
# Criando a classe Livro com parâmetros no método construtor

class Livro():

    def __init__(self, titulo, isbn):

        self.titulo = titulo

        self.isbn = isbn

        print("Construtor chamado para criar um objeto desta classe.")

    def imprime(self, titulo, isbn):

        print("Este é o livro %s e ISBN %d" %(titulo, isbn))
```

Isso garante que quando a pessoa for criar uma "instancia" de livro, tenha que passar o titulo e o ISBN em sequência

```
# Criando o objeto Livro2 que é uma instância da classe Livro

Livro2 = Livro("O Poder do Hábito", 77886611)
```
- Depois de criar o objeto Livro 2 que por consequencia é uma instancia da classe livro, temos como chamar o atributo que quisermos
```
Livro2.titulo
```
- Isso vai nos garantir que o titulo do livro 2 seja trazido

# Manipulação de Objetos em Python
Em Python, tudo é objeto.

```
# Criando uma lista

lst_num = ["Data", "Science", "Academy", "Nota", 10, 10]
```

```
# A lista lst_num é um objeto, uma instância da classe lista em Python

type(lst_num)
```

## Criando um objeto de exemplo
```
# Criando um novo tipo de objeto chamado Carro

class Carro(object):

    pass
```

```
# Instância do Carro

ferrari = Carro()
```

```
print(type(ferrari))

# <class '__main__.Carro'>
```

## Criando outro exemplo de objeto
```
# Criando uma classe

class Estudantes:

    def __init__(self, nome, idade, nota):

        self.nome = nome

        self.idade = idade

        self.nota = nota
```

```
# Criando um objeto chamado Estudante1 a partir da classe Estudantes

Estudante1 = Estudantes("Bob", 12, 9.5)
```

```
# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe

Estudante1.nome
```
Ao criar um objeto, consigo acessar os atributos assim definidos na nossa funçao construtora

## Exemplo de funcionarios

```
# Criando uma classe

class Funcionarios:

    def __init__(self, nome, salario, cargo):

        self.nome = nome

        self.salario = salario

        self.cargo = cargo

  

    def listFunc(self):

        print("Funcionário(a) " + self.nome + " tem salário de R$" + str(self.salario) + " e o cargo é " + self.cargo)

# Criando um objeto chamado Func1 a partir da classe Funcionarios

Func1 = Funcionarios("Mary", 20000, "Cientista de Dados")
```

### Utilizando método
```
# Usando o método da classe

Func1.listFunc()

#Funcionário(a) Mary tem salário de R$20000 e o cargo é Cientista de Dados
```

## Has "algo" ou Set "algo"
- Serve pra saber se tem algum atributo ou até mesmo modificar algum atributo
### hasattr
```
hasattr(Func1, "nome")

#True
```
- Serve para saber se tem esse atributo

### setattr
```
setattr(Func1, "salario", 4500)
```
- Consegue alterar o atributo

### getattr 
- Vai pegar o valor do atributo
```
getattr(Func1, "salario")
```

### delattr
- Vai deletar o atributo
```
delattr(Func1, "salario")
```
