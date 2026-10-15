# TaskTracker

Aplicação de linha de comando (CLI) para cadastro e visualização de tarefas, desenvolvida na **Fase 2 (Entrega Intermediária)** do Bootcamp II de Engenharia de Software.

## Descrição funcional

O TaskTracker oferece um menu contínuo no terminal com três opções:

1. **Cadastrar nova tarefa**: pede título, descrição, prioridade e data limite.
2. **Visualizar tarefas cadastradas**: lista todas as tarefas com todos os campos.
3. **Sair da aplicação**.

Cada tarefa é um dicionário com os campos `titulo`, `descricao`, `prioridade`, `data_limite` e `status`. As tarefas ficam em uma lista em memória durante a execução.

## Regras de validação

| Campo | Regra |
|---|---|
| Título | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e o prompt se repete até um título válido. |
| Descrição | Texto livre, pode ficar vazia. |
| Prioridade | Aceita apenas `Alta`, `Média`, `Media` ou `Baixa`, sem diferenciar maiúsculas/minúsculas. É salva sempre como `Alta`, `Média` ou `Baixa`. Valor inválido gera mensagem de erro e repete o prompt. |
| Data limite | Texto livre ou DD/MM/AAAA, sem validação rígida. |
| Status | Definido automaticamente como `Pendente` no cadastro. |

Opção de menu inválida exibe mensagem de erro e mostra o menu de novo. Se não houver tarefas, a listagem informa que não existem registros.

## Tecnologias

- Python 3 (somente biblioteca padrão)
- Git e GitHub para versionamento

## Instalação e execução

Pré-requisito: Python 3 instalado.

```bash
git clone <url-do-repositorio>
cd tasktracker-projeto
python src/main.py
```

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento lógico da Fase 1
└── src/
    └── main.py                   # Código-fonte da aplicação
```

## Evolução planejada

O planejamento da Fase 1 (`docs/planejamento_logico.pdf`) descreve também quadro Kanban, calendário por data limite e expiração automática de tarefas concluídas. Essas funcionalidades ficam como evolução planejada para as fases futuras do projeto.
