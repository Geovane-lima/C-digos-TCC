import os
import subprocess

from Blockchain import Blockchain
from AtaqueDDoS import AtaqueDDoS

def exibir_menu():
    print("\nMenu:")
    print("1. Iniciar servidor Blockchain")
    print("2. Criar Blockchain")
    print("3. Simular Ataque DDoS")
    print("0. Sair")

def main():
    blockchain = None
    server_process = None
    server_script_path = os.path.join(os.path.dirname(__file__), "server.py")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            if server_process is None:
                server_process = subprocess.Popen(["python", server_script_path])
                print("Servidor Blockchain iniciado.")
            else:
                print("Servidor Blockchain já está em execução.")
            input("Aguarde alguns instantes e aperte enter para continuar...\n\n")
        elif opcao == "2":
            if server_process is None:
                print("Por favor, inicie o servidor Blockchain primeiro (opção 1).")
            else:
                try:
                    total_blocos = int(input("Digite o número de blocos a serem criados na blockchain: "))
                    blockchain = Blockchain()
                    blockchain.run_simulacao(total_blocos)  # Passando o total de blocos como argumento
                except ValueError:
                    print("Por favor, insira um número válido.")
        elif opcao == "3":
            try:
                num_transacoes_maliciosas = int(input("Digite o número de transações maliciosas a serem simuladas: "))
                ataque_ddos = AtaqueDDoS("http://localhost:5000", num_transacoes_maliciosas)
                ataque_ddos.simular()
            except ValueError:
                print("Por favor, insira um número válido para as transações maliciosas.")
        elif opcao == "0":
            if server_process is not None:
                server_process.terminate()
                print("Servidor Blockchain encerrado.")
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()