import sqlite3

def criar_tabela():
    conexao = sqlite3.connect("financeiro.db")
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

def adicionar_transacao(tipo, descricao, valor):
    conexao = sqlite3.connect("financeiro.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO transacoes (tipo, descricao, valor) VALUES (?, ?, ?)", (tipo, descricao, valor))
    conexao.commit()
    conexao.close()

def listar_transacoes():
    conexao = sqlite3.connect("financeiro.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM transacoes")
    for linha in cursor.fetchall():
        print(linha)
    conexao.close()

def calcular_saldo():
    conexao = sqlite3.connect("financeiro.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(CASE WHEN tipo='receita' THEN valor ELSE -valor END) FROM transacoes")
    saldo = cursor.fetchone()[0]
    conexao.close()
    return saldo if saldo else 0.0

def menu():
    while True:
        print("\n=== Controle Financeiro Pessoal ===")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Listar Transações")
        print("4. Ver Saldo Atual")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da receita: ")
            valor = float(input("Valor: "))
            adicionar_transacao("receita", descricao, valor)
            print("Receita adicionada com sucesso!")
        elif opcao == "2":
            descricao = input("Descrição da despesa: ")
            valor = float(input("Valor: "))
            adicionar_transacao("despesa", descricao, valor)
            print("Despesa adicionada com sucesso!")
        elif opcao == "3":
            listar_transacoes()
        elif opcao == "4":
            print(f"Saldo atual: R$ {calcular_saldo():.2f}")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    criar_tabela()
    menu()
