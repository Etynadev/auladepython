import schedule
import time
import subprocess

# Função para executar o script de análise
def executar_analise():
    print("Iniciando a análise...")
    subprocess.run(["python", "caminho/para/o/seu/script/analise.py"])
    print("Análise concluída!")

# Agendar a execução do script de análise para todos os dias às 9h
schedule.every().day.at("09:00").do(executar_analise)

print("Agendamento configurado para executar todos os dias às 9h.")

# Loop para verificar se é hora de executar a tarefa
while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica a cada minuto se o horário de execução chegou