from plyer import notification

def lembrete(titulo, mensagem):
    notification.notify(
    title=titulo,
    message=mensagem,
    app_name='lembrete',
    timeout=10
)
lembrete("tomar medicação", " é seu tratamento")


