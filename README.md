# Códigos-TCC 🚀

Códigos desenvolvidos para simulação de ataque DDoS na rede Blockchain criada 🔐💻

## Projeto de TCC - Blockchain e Ataque DDoS 🔒⚔️

Este repositório contém o código do meu Trabalho de Conclusão de Curso (TCC) na área de **Blockchain e Ataque DDoS**. O objetivo do projeto é simular um servidor Blockchain e realizar um ataque DDoS a esse servidor para estudar as implicações de segurança. O código é dividido em diversas classes responsáveis pela criação da Blockchain, simulação do ataque DDoS e interação com o usuário.

## 🛠️ Classes Criadas

### 1. **Classe `Main`**
   A classe principal do projeto contém a lógica de interação com o usuário, incluindo o menu de opções. Ela permite:
   - Iniciar o servidor Blockchain.
   - Criar a Blockchain.
   - Simular um Ataque DDoS ao servidor.

### 2. **Classe `Blockchain`**
   A classe `Blockchain` gerencia a criação e manipulação da cadeia de blocos. Ela é responsável por:
   - Criar e adicionar blocos à blockchain.
   - Processar transações.
   - Minerar blocos com uma dificuldade ajustável.
   - Exibir estatísticas sobre a blockchain, como blocos criados, taxa de hash e eficiência.

### 3. **Classe `Bloco`**
   A classe `Bloco` é usada para representar um único bloco na cadeia de blocos da Blockchain. Cada bloco contém:
   - Transações.
   - O hash do bloco anterior.
   - Um nonce para permitir a mineração do bloco.

### 4. **Classe `AtaqueDDoS`**
   A classe `AtaqueDDoS` simula um ataque DDoS enviando múltiplas transações maliciosas para o servidor Blockchain.

### 5. **Classe `Server`**
   A classe `Server` cria um servidor web usando o Flask para hospedar a Blockchain e permitir que transações sejam enviadas para a rede. Além disso, possui rotas para:
   - Verificar o status do servidor.
   - Adicionar transações.
   - Exibir métricas do servidor (número de requisições, tempo médio de processamento, etc).
   - Retornar a cadeia de blocos.

### 6. **Classe `Transacao`**
   A classe `Transacao` define uma transação com remetente, destinatário e valor. Além disso, permite assinar a transação para garantir sua integridade.

## 🛠️ Requisitos

Certifique-se de que você já possui o Python instalado em sua máquina. Para rodar este código, você precisará instalar as seguintes dependências:

- `Flask` - Para o servidor web.
- `prettytable` - Para exibir estatísticas da blockchain em formato de tabela.
- `openpyxl` - Para exportar a blockchain para planilhas Excel.
- `pycryptodome` - Para manipulação de chaves e assinaturas digitais.
- `hashlib` - Para criar os hashes dos blocos.
  
Você pode instalar as dependências necessárias usando o `pip`. Basta rodar o seguinte comando no terminal:

```bash
pip install flask prettytable openpyxl pycryptodome

