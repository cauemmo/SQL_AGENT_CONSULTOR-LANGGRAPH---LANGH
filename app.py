from agent.sql_agent import responder
print("____________________________________________________________________________________________________________________")
print("\n\n\nAgente pronto! Faça perguntas como:\n- Quem tem saldo suficiente para comprar um Smartphone?\n- Quem comprou notebook? \nDigite 'sair' para encerrar.\n")
print("OBS: O tempo de resposta atual da consulta pode demorar um pouco,mas é normal")

while True:
    pergunta = input("Pergunta: ")
    if pergunta.strip().lower() == "sair":
        print("Até logo!")
        break

    try:
        resposta = responder(pergunta)
        print("Resposta:", resposta)
    except Exception as e:
        print("Erro ao processar:", e)
