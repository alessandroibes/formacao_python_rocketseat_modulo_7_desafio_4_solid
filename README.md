# S.O.L.I.D

Nesse desafio, é apresentado de forma prática, os conceitos aprendidos no módulo de Conceitos SOLID da Formação Python da Rocketseat.

O desafio consiste em aplicar os conceitos de Single Responsability Principle e Open Closed Principle conforme descrito abaixo:

## Single Responsability Principle

Note que na classe ``TaskHandler``, presente no arquivo ``/1_S_SRP/srp_bad_example.py``, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

[ ] Seguindo o conceito do Princípio da Responsabilidade única, essa classe deve ser reorganizada e, se necessário, deve ser criado outras classes com suas devidas responsabilidades.

## Open Closed Principle

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no códig em ``/2_O_OCP/ocp_bad_example.py`` que, conforme a clínica adiciona exames, deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle).

[ ] Utilizando do conceito do OCP, criar uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.