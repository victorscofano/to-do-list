# TO-DO List (Terminal)
Aplicação de linha de comando para gerenciamento de tarefas, escrita em **Python**. Permite adicionar, listar, concluir, editar e remover tarefas através de um menu interativo, com persistência dos dados em um arquivo *JSON* e interface colorida no terminal usando a biblioteca `rich`.

## Funcionalidades
- Adicionar tarefa
- Listar tarefas
- Marcar tarefa como concluída
- Editar tarefa
- Salvar tarefas em arquivo **JSON**
- Carregar tarefas automaticamente ao iniciar o programa
- Menu interativo no **terminal**
- Tratamento de erros (entradas inválidas, arquivos ausentes, JSON corrompido, permissões, etc.)

## Tecnologias utilizadas
- **Python 3**
- `rich` - para formatação colorida e painéis no terminal
- **Módulos nativos**: `json`, `os`, `datetime`

## Estrutura do projeto

```
to-do-list/
├── main.py             # Controla o fluxo geral do programa
├── menu.py             # Exibe o menu e captura a escolha do usuário
├── tarefas.py          # Lógica de manipulação das tarefas (adicionar, listar, concluir, editar, remover)
├── arquivo.py          # Salva e carrega as tarefas no arquivo JSON
├── data/
|   └── dados.json      # Armazena as tarefas (criado automaticamente pelo programa ao executar)
├── requirements.txt    # Dependências do projeto (apenas a biblioteca rich)
└── README.md           # Este arquivo
```

## Responsabilidades de cada módulo
| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Orquestra o programa: carrega os dados, roda o menu em loop, chama as funções corretas e salva as alterações realizadas |
| `menu.py` | Apenas exibe as opções e lê a escolha do usuário (não conhece a lógica de tarefas) |
| `tarefas.py` | Apenas manipula a lista de tarefas em memória (não sabe nada sobre arquivos ou terminal) |
| `arquivo.py` | Apenas lê e escreve o arquivo **JSON** (não sabe o que é uma tarefa) |

## Estrutura de uma tarefa
Cada tarefa é representada por um dicionário com os seguintes campos:

```python
{
    "id": 1,
    "descricao": "Estudar Python",
    "status": False,
    "data_criacao": "2026-07-06 14:30:00"
}
```
- **id**: identificador único e sequencial, gerado automaticamente (nunca reaproveitado)
- **descricao**: texto da tarefa em si
- **status**: `True` (concluída) ou `False` (pendente)
- **data_criacao**: data e hora em que a tarefa foi criada

## Instalação
1. Clone o repositório:
   
```bash
git clone 
cd to-do-list
```

2. Crie um ambiente virtual (opcional, mas recomendado):
 ```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
   ```
3. Instale dependências:
```bash
pip install -r requirements.txt
```

## Como usar
Execute o programa a partir da raiz do projeto:
```bash
python main.py
```

O menu principal será exibido:
```
======= TO-DO LIST ======

1 - Adicionar tarefa
2 - Listar tarefa
3 - Concluir tarefa
4 - Editar tarefa
5 - Remover tarefa
6 - Sair

>>
```
Basta digitar o número da opção desejada e seguir as instruções na tela. As tarefas são salvas automaticamente em `data/dados.json` a  cada alteração e carregadas automaticamente da próxima vez que o programa for iniciado.

## Tratamento de erros
O programa foi construído prevendo cenários comuns de falhas, entre eles:
- Opção de menu ou ID digitado que não seja um número válido
- Tentativa de concluir, editar ou remover um ID que não existe na lista
- Tentativa de editar uma tarefa com descrição vazia
- Arquivo `dados.json` inexistente na primeira execução (o programa inicia normalmente com a lista vazia e avisa ao usuário)
- Arquivo `dados.json` corrompido ou com conteúdo inválido
- Falta de permissão do sistema para ler ou escrever o arquivo de dados
  
## Decisões de design
- **IDs sequenciais, nunca reaproveitados**: o próximo ID é sempre o maior ID já existente + 1, mesmo que tarefas do meio da lista tenham sido removidas. Isso evita ambiguidade ao referenciar tarefas específicas.
- **Funções de `tarefas.py` sempre retornam a lista atualizada**: mesmo que a mutação de listas em Python já reflita a alteração automaticamente, manter um `return tarefas` consistente em todas as funções deixa o comportamento mais explícito e previsível.
- **Tratamento de exceções específicas**: em vez de um único `except Exception` genérico, o `arquivo.py` trata separadamente `FileNotFoundError`, `PermissionError`, `json.JSONDecodeError` e `OSError`, oferecendo mensagens mais precisas para cada tipo de falha.
- **Separação de responsabilidades entre módulos**: nenhuma função de `tarefas.py` ou `arquivo.py` usa `input()` ou `prin()` de interface - essa responsabilidade fica isolada em `menu.py` e `main.py`.

## Autor
Projeto desenvolvido como exercício de estruturação de projetos Python, manipulação de arquivos JSON e boas práticas de tratamento de erros.