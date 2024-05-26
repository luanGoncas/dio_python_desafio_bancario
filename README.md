# Desafio de Projeto: Criando um Sistema Bancário
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

## Operação de depósito
Deve ser possível depositar valores positivos para a minha conta bancária. A versão 1 do projeto trabalha apenas com 1 usuário. Dessa forma, não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de depósito - Versão 2
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: Saldo, valor, extrato. Sugestão de retorno: Saldo e extrato.

## Operação de saque

O sistema deve permitir realizar 3 saques diários com o limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de salto. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de saque - versão 2

A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: Saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

## Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

## Operação de extrato - versão 2

A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

## Operação de criação de usuário/cliente - versão 2

Criar usuário (cliente) - O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro - número - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

## Operação de criação de conta corrente - versão 2

Criar conta corrente - O programa deve armazenar contas em uma lista. Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta mas uma conta pertence somente a um usuário.