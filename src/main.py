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


def ler_titulo() -> str:
    """Pede o título até que um valor não vazio seja informado."""
    while True:
        titulo = input("Título: ")
        if validar_titulo(titulo):
            return titulo.strip()
        print("Erro: o título é obrigatório e não pode ficar vazio.")


def ler_prioridade() -> str:
    """Pede a prioridade até que Alta, Média/Media ou Baixa seja informada."""
    while True:
        prioridade = validar_prioridade(input("Prioridade (Alta, Média ou Baixa): "))
        if prioridade is not None:
            return prioridade
        print("Erro: prioridade inválida. Use apenas Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas: list[dict]) -> None:
    """Coleta os dados, cria a tarefa com status Pendente e a adiciona à lista."""
    print("\n--- Cadastrar nova tarefa ---")
    tarefa = {
        "titulo": ler_titulo(),
        "descricao": input("Descrição (opcional): ").strip(),
        "prioridade": ler_prioridade(),
        "data_limite": input("Data limite (DD/MM/AAAA ou texto livre): ").strip(),
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f"\nTarefa \"{tarefa['titulo']}\" cadastrada com sucesso!")


def listar_tarefas(tarefas: list[dict]) -> None:
    """Exibe todas as tarefas com seus campos, ou avisa se não houver nenhuma."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite'] or '(não informada)'}")
        print(f"  Status:      {tarefa['status']}")
    print(f"\nTotal: {len(tarefas)} tarefa(s).")


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
