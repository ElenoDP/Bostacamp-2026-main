# Sistema de Acompanhamento de Atendimento

## Ambulatório AME UNIMAR

## 1. Problema identificado

Foi identificado que pacientes do AME UNIMAR frequentemente não sabem quantos pacientes estão à sua frente na fila de espera ou quanto falta para serem chamados.

Essa situação pode fazer com que o paciente precise perguntar constantemente à recepção sobre sua situação, além de dificultar que ele se organize enquanto aguarda o atendimento.

## 2. Pesquisa de campo

Para compreender melhor o problema, foi realizada uma visita presencial ao AME UNIMAR.

Durante a visita, conversei com um recepcionista, que forneceu informações sobre o funcionamento da recepção e sobre dificuldades encontradas no atendimento aos pacientes.

Também foram observados pacientes e o funcionamento do local, permitindo que a proposta do sistema fosse desenvolvida de acordo com a realidade observada.

## 3. Objetivo

O objetivo do sistema é permitir que o paciente consulte sua situação na fila de espera de maneira rápida, verificando seu estado e quantos pacientes aguardando estão à sua frente.

## 4. Solução proposta

Foi desenvolvido um sistema de acompanhamento da fila de atendimento composto por uma interface para a recepção e um visor para consulta dos pacientes.

A recepção pode cadastrar pacientes e controlar as chamadas. O paciente, por sua vez, pode consultar sua situação pelo próprio nome.

Dessa forma, o sistema busca reduzir a necessidade de o paciente perguntar constantemente à recepção sobre sua posição na fila.

## 5. Funcionamento do sistema

O sistema possui duas interfaces principais.

A interface da recepção permite cadastrar pacientes, chamar o próximo paciente, rechamar o último paciente chamado e registrar uma evasão.

A interface do paciente permite informar seu nome e consultar sua situação. O sistema informa seu estado e quantos pacientes aguardando atendimento estão à sua frente.

Com essas informações, o paciente consegue se organizar melhor durante a espera, podendo, por exemplo, ir ao banheiro ou comprar um lanche sem precisar permanecer constantemente próximo à recepção.

## 6. Interface da recepção

A interface da recepção foi desenvolvida utilizando os conhecimentos de Python e Tkinter trabalhados durante o Bootcamp.

Ela possui campos e botões para realizar as operações necessárias para o controle da fila de pacientes.

A interface foi mantida simples e objetiva para facilitar sua utilização durante o atendimento.

## 7. Visor do paciente

O visor do paciente foi desenvolvido para permitir uma consulta rápida e intuitiva.

O paciente informa seu nome e recebe as informações relacionadas à sua situação na fila, incluindo seu estado atual e a quantidade de pacientes que estão à sua frente.

## 8. Estados dos pacientes

Cada paciente possui um estado que representa sua situação no sistema.

Os estados utilizados são:

* **Aguardando:** o paciente está esperando para ser chamado.
* **Chamado:** o paciente foi chamado para atendimento.
* **Evasão:** o paciente foi chamado, mas não compareceu.

A consulta do estado permite que o paciente saiba rapidamente se já foi chamado e não ouviu a chamada, podendo se dirigir à recepção ou ao local de atendimento.

## 9. Estrutura do projeto

O projeto foi dividido em arquivos para separar as responsabilidades do sistema.

* `fila.py` — contém a lógica do sistema, incluindo cadastro, fila, estados e consultas.
* `interface.py` — contém as interfaces gráficas da recepção e do paciente.
* `main.py` — responsável por iniciar o programa.

Foi utilizada Programação Orientada a Objetos para organizar as funcionalidades do sistema, além de funções, variáveis e estruturas de dados trabalhadas durante o Bootcamp.

## 10. Tecnologias utilizadas

* Python
* Tkinter

## 11. Simulação

O projeto possui uma simulação de funcionamento demonstrando o cadastro de pacientes, controle da fila e consulta da situação do paciente.

O vídeo de apresentação e demonstração está incluído no arquivo `.ZIP` enviado para a submissão.

## 12. Limitações

Atualmente, o sistema é um protótipo desenvolvido para demonstrar a solução proposta.

Os dados são mantidos apenas durante a execução do programa e não são armazenados permanentemente. Em uma versão destinada a utilização real, o sistema poderia ser aperfeiçoado com armazenamento de dados, integração com os processos existentes e outras funcionalidades.

## 13. Demonstração

A demonstração do sistema pode ser conferida no vídeo de apresentação enviado junto ao código-fonte.


## LINK DO VIDEO
https://www.youtube.com/watch?v=xrnVY4ydAkg
