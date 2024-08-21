

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

#classe
# Trabalhando com Métodos de Classes em Python
Em Python, os métodos de classes são funções definidas dentro de uma classe, que realizam operações específicas em objetos criados a partir dessa classe. Os métodos de classes são usados para implementar o comportamento dos objetos que pertencem a essa classe.



Assim como as funções em Python, os métodos de classes podem receber argumentos e retornar valores. No entanto, diferentemente das funções normais, os métodos de classes sempre incluem o parâmetro self como o primeiro argumento, que é usado para se referir ao objeto atual da classe.

  

O método __init__ é um método especial que é chamado quando um objeto é criado a partir da classe. Este método é usado para inicializar os atributos do objeto. Outros métodos podem ser definidos para executar tarefas específicas em um objeto, como calcular valores, realizar operações de entrada e saída, ou alterar o estado do objeto.

## Exemplo

```
# Criando uma classe chamada Circulo

class Circulo():

    # O valor de pi é constante

    pi = 3.14

  

    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5.

    def __init__(self, raio = 5):

        self.raio = raio

  

    # Esse método calcula a área.

    def area(self):

        return (self.raio * self.raio) * Circulo.pi

  

    # Método para gerar um novo raio

    def setRaio(self, novo_raio):

        self.raio = novo_raio

  

    # Método para obter o raio do círculo

    def getRaio(self):

        return self.raio
```

```
# Criando outro objeto chamado circ1. Uma instância da classe Circulo()

# Agora sobrescrevendo o valor do atributo

circ1 = Circulo(7)
```

#heranca

# Trabalhando com Herança de Classes em Python

  

Em Programação Orientada a Objetos (POO), a herança é um conceito que permite criar novas classes a partir de outras classes existentes, aproveitando os atributos e métodos da classe original e adicionando novos atributos e métodos específicos.


A classe original é chamada de classe mãe ou superclasse e a nova classe criada é chamada de classe filha ou subclasse.


A herança é uma técnica importante em POO porque permite reutilizar o código de maneira eficiente. Em vez de criar uma nova classe do zero, a subclasse pode herdar todos os atributos e métodos da superclasse e adicionar apenas o que é necessário. Dessa forma, a subclasse pode se concentrar em fornecer funcionalidades adicionais sem precisar se preocupar com as características básicas da classe.


Na herança, uma subclasse pode herdar os atributos e métodos da superclasse e substituí-los ou estendê-los conforme necessário. Por exemplo, uma subclasse pode ter um método com o mesmo nome de um método da superclasse, mas com um comportamento diferente.

## Criando a super-classe

```
# Criando a classe Animal - Super-classe

class Animal:

    def __init__(self):

        print("Animal criado.")

  

    def imprimir(self):

        print("Este é um animal.")

  

    def comer(self):

        print("Hora de comer.")

    def emitir_som(self):

        pass
```
- Observe que o método "emitir_som" ele foi criado, porem nao tem funcionalidade
- Sera feito em sequencia
```
# Criando a classe Cachorro - Sub-classe

class Cachorro(Animal):

    def __init__(self):

        Animal.__init__(self)

        print("Objeto Cachorro criado.")

    def emitir_som(self):

        print("Au au!")
```
- Nessa classe Cachorro, temos uma sub-classe de animal.
- Herda todos os metodos da classe animal, por isso a heranca

```
# Criando um objeto (Instanciando a classe)

rex = Cachorro()]


#Animal criado. 
#Objeto Cachorro criado.
```

Agora é possível chamar todos os atributos
```
rex.emitir_som()

#Au au!
```

```
# Executando o método da classe Cachorro (sub-classe)

rex.imprimir()

#Este é um animal.
```


# Trabalhando com Polimorfismo de Classes em Python


Polimorfismo é um dos conceitos fundamentais da Programação Orientada a Objetos (POO). O polimorfismo permite que objetos de diferentes classes possam ser tratados de forma uniforme. Isso significa que um objeto pode ser tratado como se fosse um objeto de uma superclasse, mesmo que ele seja de uma subclasse.


Mais especificamente, o polimorfismo se refere à habilidade de um objeto responder de diferentes formas a uma mesma mensagem. Isso é possível porque as subclasses podem implementar métodos com o mesmo nome que os métodos da superclasse, mas com comportamentos diferentes.


Com o Polimorfismo, os mesmos atributos e métodos podem ser utilizados em objetos distintos, porém, com implementações lógicas diferentes.


```
# Superclasse

class Veiculo:

    def __init__(self, marca, modelo):

        self.marca = marca

        self.modelo = modelo

  

    def acelerar(self):

        pass

  

    def frear(self):

        pass
```

```
# Subclasse

class Carro(Veiculo):

    def acelerar(self):

        print("O carro está acelerando.")

  

    def frear(self):

        print("O carro está freando.")
```

```
# Subclasse

class Moto(Veiculo):

    def acelerar(self):

        print("A moto está acelerando.")

  

    def frear(self):

        print("A moto está freando.")
```

```
# Subclasse

class Aviao(Veiculo):

    def acelerar(self):

        print("O avião está acelerando.")

  

    def frear(self):

        print("O avião está freando.")

  

    def decolar(self):

        print("O avião está decolando.")
```
## Entenda Polimorfismo !

### Primeiro
- Cria-se uma superclasse que e responsavel por ter um construtor padrao para  as outras subclasses
- cria-se metodos personalizaveis para as futuras subclasses
## Segundo
- Criacao das subclasses com seus proprio metodo
## Terceiro
- Cria-se agora acoes que possuem o mesmo nome, utilizando o polimorfismo
```
# Cria os objetos

lista_veiculos = [Carro("Porsche", "911 Turbo"), Moto("Honda", "CB 1000R Black Edition"), Aviao("Boeing", "757")]
```

```
# Loop

for item in lista_veiculos:

    # O método acelerar tem comportamento diferente dependendo do tipo de objeto

    item.acelerar()

    # O método frear tem comportamento diferente dependendo do tipo de objeto

    item.frear()

  

    # Executamos o método decolar somente se o o objeto for instância da classe Aviao

    if isinstance(item, Aviao):

        item.decolar()

  

    print("---")
```