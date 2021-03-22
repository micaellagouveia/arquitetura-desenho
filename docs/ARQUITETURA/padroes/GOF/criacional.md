# GoF Criacional (GoF - Gang of Four)
Solução consolidada para um problema recorrente no desenvolvimento e manutenção de software orientado a objetos.

## Factory Method
* Encapsular a escolha da classe concreta a ser utilizada na criação de objetos de um determinado tipo

*Definir uma interface para criar um objeto, mas deixar as subclasses decidirem que classe instanciar*

* Tem como objetivo principal definir uma interface de criação de objetos e cada subclasse fica responsável pela criação do objeto..
* Com o uso desse padrão, os objetos não são definifos através de uma classe concreta (para isso é definida a interface).

As classes nesse diagrama sao:
1. **Product**: Define a interface para objetos que o método de fábrica cria. *(Exemplo: Documento)*
    * Define atributos e métodos. Esses últimos abstratos ou programados de forma mais genérica, para um conjunto de objetos, o squais serão criados pelo factoryMethod().
2. **ConcreteProdutc**: implementa a interface Product. *(Exemplo:Relatório, Currículo)*
    * Estende Product, especializamdo o que foi definido na superclasse.
3. **Creator**(também chamada de Factory pois cria os objetos de Product): declara o método factoryMethod() que retorna um objeto de Product. Pode chamar o método gerador para criar objetos do Product. *(Exemplo: Página)*    
    * Declara o factoryMethod(), o qual retorn um objeto do tipo Product. Pode definir também um implementação default do factoryMethod() que retorna um objeto ConcreteProduct default. Pode ainda chamar um factoryMethod() para criar um objeto de Product.
4. **ConcreteCreator**: sobrescreve o método gerador para criar objetos ConcreteProduct. *(Exemplo: PáginaDeHabilidades, PaginaProfissional, ...)*
    * Sobrescreve o factory method para retornar uma instância de ConcreteProduct.

![factory method](../imagens/factoryMethod.png)


* Abstract Factory
    * Encapsular a escolha das classes concretas a serem utilizadas na criação de objetos de diversas famílias
* Builder
    * Separar o processo de contrução de um objetode sua apresetação e permitir a criação passo a passo. Diferentes tipos de objetos podem ser criados com implementações distintas de cada passo.
* Prototype (muito utilizado em jogos)
    * Possibilitar a criação de novos objetos a partir da cópia de objetos existentes
* Singleton
    * Permitir a criação de uma única instância de um classe e fornecer um modo de recuperá-la.
* Multiton
    * Permitir a criação de uma quantidade limitada de instâncias de determinada classe e fornecer um modo para recuperá-las.
* Object Pool (muito utilizado em jogos)
    * Possibilitar o reproveitamento de objetos.
