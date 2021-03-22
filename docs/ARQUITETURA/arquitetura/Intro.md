# Arquiteturas

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

