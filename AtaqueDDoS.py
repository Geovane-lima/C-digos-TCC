import logging
import time
import requests

class AtaqueDDoS:
    def __init__(self, server_url, num_transacoes_maliciosas):
        self.server_url = server_url
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.request_times = []
        self.data_sent = 0  # Total de dados enviados
        self.data_received = 0  # Total de dados recebidos
        self.num_transacoes_maliciosas = num_transacoes_maliciosas  # Número de transações maliciosas

    def check_server(self):
        try:
            response = requests.get(f"{self.server_url}/health")
            response.raise_for_status()
            print("Servidor está disponível.")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Erro ao verificar o servidor: {e}")
            print("Servidor não está disponível. Verifique se o servidor está rodando e acessível.")
            return False

    def simular(self):
        if not self.check_server():
            print("Servidor não está disponível. Verifique se o servidor está rodando e acessível.")
            return

        print("Simulando ataque DDoS...")

        # Simula as transações maliciosas conforme o número fornecido pelo usuário
        for i in range(self.num_transacoes_maliciosas):
            try:
                start_time = time.time()
                response = requests.post(f"{self.server_url}/add_transaction", json={"transacao": None})
                end_time = time.time()
                request_time = end_time - start_time
                self.total_requests += 1
                self.request_times.append(request_time)
                self.data_sent += len(str({"transacao": None}))
                self.data_received += len(response.content)

                if response.status_code == 201:
                    self.successful_requests += 1
                    print(f"{i + 1}/{self.num_transacoes_maliciosas}: Transação maliciosa adicionada com sucesso. Tempo da requisição: {request_time:.4f} segundos.")
                else:
                    self.failed_requests += 1
                    print(f"{i + 1}/{self.num_transacoes_maliciosas}: Falha ao adicionar transação. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                self.failed_requests += 1
                print(f"Erro durante a requisição {i + 1}/{self.num_transacoes_maliciosas}: {e}")
            time.sleep(0.1)  # Ajustar conforme necessário

        print("Ataque DDoS concluído.")

        # Exibir métricas
        self.exibir_metricas()

        # Esperar até o usuário pressionar Enter para sair
        input("\nPressione Enter para continuar...")

    def exibir_metricas(self):
        if self.request_times:
            min_time = min(self.request_times)
            max_time = max(self.request_times)
            print("\nPadrão de Transação:")
            print(f"- Tempo Mínimo de Requisição: {min_time:.4f} segundos")
            print(f"- Tempo Máximo de Requisição: {max_time:.4f} segundos")

        # Volume de Dados
        print("\nVolumes de Dados:")
        print(f"- Dados Enviados: {self.data_sent} bytes")
        print(f"- Dados Recebidos: {self.data_received} bytes")

        # Disponibilidade de Serviço
        print("\nDisponibilidade de Serviço:")
        print(f"- Transações Bem-Sucedidas: {self.successful_requests}")
        print(f"- Total de Transações: {self.total_requests}")
        
        if self.total_requests > 0:
            availability = (self.successful_requests / self.total_requests) * 100
            print(f"- Disponibilidade: {availability:.2f}%")

if __name__ == "__main__":
    # URL do servidor que será atacado
    server_url = 'http://localhost:5000'

    # Solicitar o número de transações maliciosas do usuário
    num_transacoes_maliciosas = int(input("Digite o número de transações maliciosas a serem simuladas: "))

    # Inicializa a classe
    ddos = AtaqueDDoS(server_url, num_transacoes_maliciosas)

    # Realiza o ataque DDoS
    ddos.simular()