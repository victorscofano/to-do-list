from rich import print
from rich.panel import Panel


def exibir_menu():
    """
        Função que exibe o menu da To-DO LIST.
            => Recebe o input da escolha do usuário e verifica
                - A: se o input for válido, ou seja, for um número inteiro entre 1 e 6, retorna essa escolha.
                - B: se for inválido, retorna o valor fixo -1, que tipicamente está fora do range.
    """
    conteudo_menu = (
        "[bold white]\n======= TO-DO LIST ======[/bold white]\n\n"
        "[bright_green]1 - Adicionar tarefa[/bright_green]\n"
        "[bright_cyan]2 - Listar tarefa[/bright_cyan]\n"
        "[bright_blue]3 - Concluir tarefa[/bright_blue]\n"
        "[yellow]4 - Editar tarefa[/yellow]\n"
        "[red]5 - Remover tarefa[/red]\n"
        "[bright_red]6 - Sair[/bright_red]"
    )
    print(conteudo_menu)

    escolha = input(">> ")

    try:
        escolha = int(escolha)
        return escolha

    except ValueError:
        print("Opção inválida")
        return -1