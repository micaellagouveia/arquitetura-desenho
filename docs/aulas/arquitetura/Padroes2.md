## Padrões Arquiteturais

### MVC (Model View Controller)
Esse padrão separa a apresentação e ainteração de dados do sistema. Ele é estruturado em três camadas lógicas, as quais interagem entre si.

* **Model**: Detém a funcionalidade principal bem como os dados associados a cada entidade de domínio.
    * Encapsula estado da aplicação
    * *Notifica View de mudanças de estado*
* **View**: Lida com a exibição dos dados que são apresentados ao usuário.
    * Modelo renders
    * *Solicita atualização de models*
    * Envia eventos de usuário para controller.
* **Controller**: Gerencia a interaçao dos usuários e faz o intermédio das interações entre View e Model.
    * Mapeia ações de usuários para atualizar modelo.
    * Seleciona views

É usado quando existe várias maneiras de se visualizar e interagir com dados, também quando são desconhecidos os futuros requisitos de interação e apresentação de dados. É usado quando há necessidade de várias interfaces com o usuário, e/ou de várias visões de dados e/ou até de mudanças nos dados constantes.

### Estrutura Model
* Funcionalidade principal da aplicação
* Associar-se às controllers
* COnter os dados das entidades de domínio

### Estrutura View
* Criar e inicializar a controller associada
* Exibir informações ao usuário
* Implementar procedimento de atualização
* Recuperar dados da Model, sendo essa ação preferencialmente intermediada via Controller.

### Estrutura Controller
* Receber a entrada de dados e as requisições do usuário
* Transformar as requisições dos usuários em requisições à model
* Implementar o procedimento de atualização, se necessário.

| Vantagens | Desvantagens |
| - | - |
| Permite que os dados sejam alterados de forma independente de sua representação e vice-versa| Quando um modelo e as interfaces são simples, pode envolver o código adicinoal e maior complexidade de código desnecessária |
| Apoia a apresentação dos mesmos dados de maneiras diferentes, ou seja, múltiplas viwes de uma mesma model | Controllers e Views tendem a ser bem acopladas|
| Views sincronizadas| |
| Organização clara de abstrações ||

**Padrões de Projeto associados:**
1. GRASP (indireção e controller)
2. GoF Estrutural (Facade)
3. GoF Comportamental (Observer)