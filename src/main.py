"""TaskTracker: aplicação CLI para cadastro e visualização de tarefas."""

# Entradas aceitas (em minúsculas) mapeadas para a forma canônica salva na tarefa
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


def validar_titulo(titulo: str) -> bool:
    """Retorna True se o título não for vazio nem composto só de espaços."""
    return titulo.strip() != ""


def validar_prioridade(prioridade: str) -> str | None:
    """Retorna a prioridade na forma canônica, ou None se for inválida."""
    return PRIORIDADES_VALIDAS.get(prioridade.strip().lower())


def exibir_menu() -> None:
    """Exibe as opções do menu principal."""
    print("\n===== TASKTRACKER =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def cadastrar_tarefa(tarefas: list[dict]) -> None:
    """Cadastra uma nova tarefa (em construção)."""
    print("\n[Em construção] Cadastro de tarefas.")


def listar_tarefas(tarefas: list[dict]) -> None:
    """Exibe as tarefas cadastradas (em construção)."""
    print("\n[Em construção] Listagem de tarefas.")


def main() -> None:
    """Executa o loop principal do menu até o usuário escolher sair."""
    tarefas: list[dict] = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nSaindo do TaskTracker. Até logo!")
            break
        else:
            print("\nErro: opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
