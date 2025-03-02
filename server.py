import logging
import time
from flask import Flask, request, jsonify
from Blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DDoS_Simulation_Server")

total_requests = 0
successful_requests = 0
failed_requests = 0
total_processing_time = 0

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='healthy'), 200

@app.route('/')
def index():
    return "Servidor Blockchain em execução", 200

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    global total_requests, successful_requests, failed_requests, total_processing_time

    data = request.get_json()
    start_time = time.time()

    try:
        blockchain.adicionar_transacao(data['transacao'])
        end_time = time.time()

        processing_time = end_time - start_time
        total_requests += 1
        successful_requests += 1
        total_processing_time += processing_time

        logger.info(f"Transação adicionada. Tempo de processamento: {processing_time:.4f} segundos.")
        return jsonify({"message": "Transação adicionada."}), 201
    except KeyError as e:
        end_time = time.time()

        processing_time = end_time - start_time
        total_requests += 1
        failed_requests += 1

        logger.error(f"Erro ao adicionar transação: {e}. Tempo de processamento: {processing_time:.4f} segundos.")
        return jsonify({"message": "Falha ao adicionar transação. Campo 'transacao' ausente."}), 400
    except Exception as e:
        end_time = time.time()

        processing_time = end_time - start_time
        total_requests += 1
        failed_requests += 1

        logger.error(f"Erro ao adicionar transação: {e}. Tempo de processamento: {processing_time:.4f} segundos.")
        return jsonify({"message": "Falha ao adicionar transação."}), 500
    
@app.route('/metrics', methods=['GET'])
def get_metrics():
    global total_requests, successful_requests, failed_requests, total_processing_time

    if total_requests > 0:
        average_processing_time = total_processing_time / total_requests
    else:
        average_processing_time = 0

    metrics = {
        "total_requests": total_requests,
        "successful_requests": successful_requests,
        "failed_requests": failed_requests,
        "average_processing_time": average_processing_time
    }

    return jsonify(metrics), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    chain_data = [bloco.__dict__ for bloco in blockchain.cadeia]
    return jsonify({"length": len(chain_data), "chain": chain_data}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)