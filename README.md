
# Fila de Atendimento

Este é um sistema simples de gestão de fila de atendimento que prioriza gestantes, crianças de colo e idosos, com base em um sistema de prioridades. O sistema permite adicionar pessoas à fila, atender a próxima pessoa com a maior prioridade, visualizar a fila atual e realizar buscas específicas.

## Funcionalidades

- **Adicionar pessoas à fila:** Adiciona pessoas com informações como nome, idade, se é gestante ou criança de colo.
- **Atender próxima pessoa:** A pessoa com a maior prioridade é atendida primeiro, considerando as condições de gestante, criança de colo e idade.
- **Mostrar fila:** Exibe a fila atual, ordenada por prioridade e ordem de chegada.
- **Buscar pessoa por nome:** Busca e exibe os dados de uma pessoa específica na fila.
- **Estatísticas da fila:** Exibe estatísticas gerais sobre a fila, como total de pessoas, número de gestantes, crianças de colo, idosos, e a distribuição por prioridade.

## Estrutura do Código

- **Função `adicionando_na_fila`:** Adiciona uma pessoa na fila, calculando a prioridade com base na idade, gestante e criança de colo.
- **Função `calculo_prioridade`:** Determina a prioridade da pessoa com base em sua idade, se é gestante ou criança de colo.
- **Função `tempo_atendimento`:** Define o tempo de atendimento de acordo com a categoria da pessoa (gestante, criança de colo, idoso ou adulto).
- **Função `atender_proxima_pessoa`:** Atende a próxima pessoa da fila com maior prioridade.
- **Função `mostrar_fila`:** Exibe a lista de pessoas na fila ordenada por prioridade.
- **Função `buscar_pessoa`:** Permite buscar uma pessoa na fila pelo nome.
- **Função `mostrar_estatisticas`:** Exibe as estatísticas da fila, como a quantidade de gestantes, crianças de colo, idosos e a distribuição por prioridades.

## Como Usar

1. Clone o repositório ou baixe os arquivos.
2. Abra o terminal/console na pasta do projeto.
3. Execute o script:

   ```bash
   python simulador_fila.py
   ```

4. O sistema irá apresentar um menu de opções. Escolha a opção desejada para adicionar pessoas à fila, atender a próxima pessoa, buscar uma pessoa, ou ver as estatísticas.

## Exemplo de Uso

### Menu de opções:

```
===== MENU =====

1. Adicionar pessoa na fila
2. Atender próxima pessoa
3. Mostrar fila
4. Buscar pessoa por nome
5. Estatísticas
6. Sair
```

### Exemplo de Adição de Pessoa à Fila:

```
Nome: João
Idade: 34
Gestante? (s ou n): n
Criança de colo? (s ou n): n
```

### Exemplo de Saída ao Atender a Próxima Pessoa:

```
Atendendo João... (tempo: 2 min)
```

### Estatísticas:

```
📊 Estatísticas da Fila:
Total de pessoas: 2
 - Idosos: 0
 - Gestantes: 0
 - Crianças de colo: 1
Idade média: 23.0 anos
Distribuição por prioridade:
 - Prioridade 1: 1 pessoa(s)
 - Prioridade 2: 1 pessoa(s)
Próxima pessoa a ser atendida: João (Prioridade 2)
```

## Tecnologias

Este projeto foi desenvolvido com Python.

## Contribuições

Sinta-se à vontade para fazer melhorias ou sugestões para o projeto. Você pode fazer um fork deste repositório, criar uma branch, fazer suas mudanças e enviar um pull request.
