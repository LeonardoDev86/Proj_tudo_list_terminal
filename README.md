# Gerenciador de Tarefas em Python(terminal)

Este é um projeto simples de um Gerenciador de Tarefas (To-Do List) desenvolvido em Python, focado em organização, modularização e persistência de dados. O sistema permite que o usuário gerencie suas atividades diárias através de uma interface de linha de comando simples e intuitiva.

## Funcionalidades

- **Adicionar Tarefas:** Permite inserir novas tarefas na lista.
- **Listar Tarefas:** Exibe todas as tarefas cadastradas com seus respectivos índices.
- **Remover Tarefas:** Exclui uma tarefa específica após confirmação do usuário.
- **Persistência de Dados:** As tarefas são salvas automaticamente em um arquivo, garantindo que os dados não sejam perdidos ao fechar o programa.
- **Interface Limpa:** Uso de comandos para limpar o terminal e organizar a visualização.

## Tecnologias Utilizadas

- **Linguagem:** [Python 3](https://www.python.org/)
- **Módulos Internos:** `os`, `json`.
- **Conceitos Aplicados:** Modularização, loops de repetição, tratamento de erros, manipulação de arquivos e persistência de dados. 

## Estrutura do Projeto

projeto_to_do_list/
├── main.py              # Fluxo principal e interface do usuário
├── todo_list/           # Pacote do sistema
│   └── funcoes.py       # Lógica de negócio, validações e persistência
└── tarefas.json         # Banco de dados em formato JSON

## Como executar

1. Clone o repositório ou baixe os arquivos.
2. Certifique-se de ter o Python instalado.
3. No terminal, dentro da pasta do projeto, execute:

```bash
   python main.py
```

*"Este projeto faz parte dos meus estudos de Python, onde apliquei conceitos de tratamento de exceções, organização de código em módulos separados e persistência de dados."*

