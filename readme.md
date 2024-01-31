# Sistema de Aluguel de Carros

## Funcionalidades

As features variam de acordo com o tipo de usuário cadastrado no sistema.

### Sem login no sistema

Sem um cadastro no sistema,o usuário pode:

#### Listar carros

O usuário pode visualizar todos os carros disponíveis e indisponíveis para aluguel.

#### Buscar carros

O usuário pode fazer uma busca por carros baseada em parâmetros opcionais.

#### Logar-se no sistema

O usuário se logar na sua conta no sistema com um id e senha.

### Usuário Comum

Uma vez que o usuário se loga no sistema, além das duas primeiras features, ele tem acesso às seguintes funcionalidades:

#### Alugar veículo

O usuário pode alugar um veículo, tornando-o seu até que o devolva.

#### Devolver veículo

Uma vez tendo alugado um veículo, é possível ao usuário devolvé-lo.

#### Ver veículos alugados

O usuário pode ver os veículos que ele mesmo alugou.

#### Deslogar no sistema

O usuário pode sair da sua conta, encerrando a sessão.

### Usuário Admin

O esse tipo de conta permite ao usuário o mesmo acesso às funcionalidades de um Usuário Comum, algumas dessas agora com uso expandido, além de outras features, como cadastro de veículo ou usuário.

#### Cadastrar carro ou usuário

O usuário Admin pode cadastrar um veículo ou um novo usuário no sistema.

#### Editar dados de veículos ou de usuário 

O usuário Admin pode alterar dados de um veículo ou de um usuário no sistema.

#### Remover dados de veículos ou de usuário 

O usuário Admin pode remover um veículo ou um usuário do sistema.

#### Alugar ou devolver carros de qualquer usuário

O usuário Admin pode alugar para qualquer usuário, assim como pode devolver veículos que qualquer usuário possa ter alugado.

#### Listar usuários

O usuário Admin pode visualizar os dados de todos os usuários.