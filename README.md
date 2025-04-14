# 🧠 Agente SQL com LangChain, PostgreSQL e Ollama

### Tabela de Conteúdos
- [Contexto e Visão Geral](#contexto-e-visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-Requisitos e Instalação](#pré-requisitos-e-instalação)
- [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Validação e Segurança](#validação-e-segurança)
- [Melhorias Futuras](#melhorias-futuras)
- [Autor](#autor)

---

## Contexto e Visão Geral

Este projeto implementa um **Agente SQL inteligente**, capaz de entender perguntas feitas em **linguagem natural (português)** e transformá-las em **consultas SQL válidas e seguras** para um banco PostgreSQL. O agente utiliza o **LangChain** com o modelo **Mistral** rodando localmente via **Ollama**.

Esse sistema é útil para analistas, equipes de dados ou empresas que desejam consultar um banco de dados real sem escrever SQL diretamente.

---

## Tecnologias Utilizadas

- **Python 3.10+**
- **LangChain**
- **LangChain Community Tools**
- **LangChain Ollama**
- **PostgreSQL**
- **Ollama + Modelo Mistral**
- **python-dotenv**
- **psycopg2**

---

## Pré-Requisitos e Instalação

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/sql-agent.git
cd sql-agent

### 2. Criar Ambiente Virtual

### 3. Ativar Ambiente Virtual
### 4. Instalar as Dependências
### 5. Criar o arquivo .env
### 6. Instalar e rodar o Ollama

## Configuração do Banco de Dados
O projeto depende de um banco PostgreSQL com as seguintes tabelas e relacionamentos:
### 1. Tabelas:
clientes
id, nome, saldo

produtos
id, nome, preco

transacoes
id, cliente_id, produto_id, data

### 2. Relacionamentos:
Um cliente pode ter várias transações (1:N)
Cada transação está associada a um único produto (N:1)

## Como Executar o Projeto
Com o ambiente ativado e o Ollma Rodando:

Você poderá fazer perguntas como: "Quem comprou um notebook?"
Exemplo de resposta : • Cliente: Alice – Produto: Notebook – Valor: R$ 2500  

## Validação e Segurança
O projeto implementa práticas para garantir segurança e estabilidade:

Validação de queries via sql_db_query_checker

Temperatura configurada para 0.0 (respostas consistentes)

Tratamento de erros com handle_parsing_errors=True

Sanitização automática da entrada com o toolkit do LangChain

## Melhorias Futuras
Criar uma interface visual com Streamlit

Otimizar a velocidade das consultas e reduzir tempo de resposta

Implementar cache de perguntas frequentes

Incluir LangGraph para visualizar o fluxo do agente

Melhorar a formatação da resposta (ex.: tabelas HTML ou Markdown)

## Autor
Desenvolvido por Cauê Mendonça Magela
Este projeto pode ser usado como base para soluções reais de NLP + SQL.
Sinta-se à vontade para contribuir, adaptar ou entrar em contato!
