import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.prompts import ChatPromptTemplate
from agent.prompt_template import prefixo, sufixo

# Carrega .env
load_dotenv()


host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
db_name = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = quote_plus(os.getenv("POSTGRES_PASSWORD"))

# Conexão bd
db_uri = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
db = SQLDatabase.from_uri(db_uri)

# Inicializa modelo 
llm = OllamaLLM(model="mistral", temperature=0)


toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Prompt customizado
prompt = ChatPromptTemplate.from_messages([
    ("system", prefixo),
    ("human", sufixo),
])

# Criação do agente
agent_executor = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True,
    agent_kwargs={"prompt": prompt}
)

def responder(pergunta):
    try:
        resposta = agent_executor.invoke({"input": pergunta})
        texto = resposta.get("output", resposta)

        # Filtra o trecho final se contiver "Final Answer:"
        if "Final Answer:" in texto:
            texto = texto.split("Final Answer:")[-1].strip()

        # Formatação em bullets
        linhas = texto.split("\n")
        bullets = [f"• {linha.strip()}" for linha in linhas if linha.strip()]
        return "\n".join(bullets)

    except Exception as e:
        return f"Erro ao processar: {e}"