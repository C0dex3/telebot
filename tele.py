import telebot
keylink = ""
bot = telebot.TeleBot(keylink)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
        texto = """"""

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
	bot.send_message(mensagem.chat.id, "Mande uma reclamação para alllla@proton.me")
	
@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
	bot.reply_to(mensagem, "Codexe recebeu o abraço")

def verificar(mensagem):
	return True

@bot.message_handler(func=verificar)
def responder(mensagem):
	texto = """Escolha uma opção para continuar(CLique no item):
/opcao1 Fazer pedido
/opcao2 reclamar de um pedido
/opcao3 mandar um abraço pro codexepy
Responde outra coisa ira resultar em nada, apenas clique em algumas das opçoes"""
	bot.reply_to(mensagem, texto)

bot.polling()
