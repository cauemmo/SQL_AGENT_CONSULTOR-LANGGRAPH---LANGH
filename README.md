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

