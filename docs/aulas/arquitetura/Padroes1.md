# Arquiteturas e Padrões Arquiteturais

## Arquiteturas Monolíticas
* Processamento centralizado
* Terminais 'Burros'
* Redes de comunicação mais lentas
* Sistema Timesharing
* Funcionalidades realizadas em um único processo em uma única instância de servidor e sua escalabilidade é conferida por replicação.
* Complicado extrair algo, uma funcionalidade legada, de forma escalável. Complicado incorporar algo, uma nova funcionalidade de forma escalável.

| Vantagens | Desvantagens |
|-----------|--------------|
| Facilidade de gerência, seja em termos de segurança, controle de usuários e de aplicações |  Interface com o usuário limitada e usuário sem autonomia  |
|  | Arquiteturas de hardware, software e comunicação, normalmente, proprietárias, levando à dependência do fornecedor |
|  | Processamento centralizado, dificultando muito a questão de escalabilidade |
|  | Alto custo de manutenção e evolução |


## Arquiteturas Distribuídas
* Serviores de serviços compartilhados com boa capacidade de processamento.
* Estações de trabalho com bom poder de processamento, rodando aplicações locais, e sendo acessadas via interfaces gráficas.
* Redes com boa velocidade

| Vantagens | Desvantagens |
|-----------|--------------|
| Usuário com autonomia | Sobrecarga da rede, pois as aplicações são executadas em estações, independentes, mas o acesso aos arquivos é feito em servidores|
| Interfaces com o usuário montada localmente e com recursos gráficos| Dificuldade de gerência, seja em termos de segurança, controle de usuários e aplicações|
| Processamento espalhado, permitindo o uso das aplicações nas estações| |
| Arquiteturas de software e comunicação podem ser proprietárias mas com recursos de integração entre plataformas||


## Estilos Arquiteturais
Uma arquitetura de software pode orientar-se por um estilo arquitetural. Trata-se de um conjunto de padrões, os quais procuram impor um determinado grau de uniformidade à arquitetura. São componentes e conectores específicos que funcionam como base
Expressa:
* Uma organização estrutural.
* Um conjunto pré-definido de substemas e suas responsabilidades
* Inclui regras e diretrizes para organizar o relacionamento entre os subsistemas

**Exemplos:** Stand-alone, Cliente-servior, P2P, Objetods Distribuídos, N-camadas, Filtros e Dutos, Repositório, Orientado a Eventos(Publisher/Subscriber), Orientado a Serviços(SOA).

### Stand-Alone
Mais simples dos estilos arquiteturais. Basicamente, baseia-se em projetar uma solução autossuficiente, a qual não depende de terceiros. Normalmente, esses terceiros são servidores especializados em fornecer serviços e/ou conteúdos.
* Estilo indicado para projeto mais simples. Quando complexos, os prjetos podem demandar soluções distribuídas, com comunicações entre clientes e servidores, P2P ou outro.

| Vantagens | Desvantagens|
| - | - |
| Simplicidade| Limitação da capacidade do projeto de expandir|

### N-Camadas
Usado para modelar a interface dos subsistema, organiza o sistema em um conjunto de camadas, cada uma das quais fornece um conjunto de serviços. Esse padrão apoia o desenvolvimento incremental de subsistemas em diferentes camadas, e quando uma camada é alterada, normalmente, apenas a camada adjacente é afetada.

*Modelo OSI*
![n-camadas](../../imagens/nCamadas.png)

**CUIDADOS:**
* As camadas de níveis superiores dependem das camadas de níveis inferiores.
* Partes do sistema devem permitir serem trocadas
    * Trocar a camada de Comunicação
    * Trocar a camada de acesso
* Podem existir várias camadas em um mesmo nível de abstração, dependendo de camadas inferiores.

**DIRETRIZES:**
* Procure estruturar o sistema em camadas, sobrepondo as mesma em níveis de abstração diferentes.
* Lembre-se que os serviços da camada X, se dependentes de algo, que essa dependência esteja, preferencialmente restrita à camada X-1. (**Arquitetura Restrita**)
* Se houver necessidade de depender de mais de uma camada inferior (**Arquitetura Relaxada**)
* O inverso, ou seja, camadas inferiores dependerem de camadas superiores não é desejado!

| Vantagens | Desvantagens|
| - | - |
| Reutilização de Camadas | Cascateamento de alterações para as camadas superiores, quando o comportamento de uma camada inferior sobre alteração /adaptações
| Dependências tendem a permanecer locais| 
| Flexibilidade para organizar multi-níveis de abstração| 
| Permite trabalhar com sistemas de dinâmicas complexas |