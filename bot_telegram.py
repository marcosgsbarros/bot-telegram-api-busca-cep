from telebot import TeleBot
import requests

token = '5572283137:AAHf7CPbmfZOEgvWsD0fqCL6t4kV51ql56E'
chat_id = 435860893
bot = TeleBot(token)

bot.send_message(chat_id,'Digite o cep para localizar o endereço: ')

@bot.message_handler(content_types=['text'])
def iniciar_bot(msg):
    verificar(msg.text)

def verificar(cep):
    if len(cep) == 8:
        get_info_cep(cep)
    else:
        bot.send_message(chat_id,'Cep inválido, digite novamente')

def get_info_cep(cep):
    try:
        url_cep = f'https://viacep.com.br/ws/{cep}/json/'
        resposta = requests.get(url_cep)
        r = resposta.json()
        responder(r)
    except:
        bot.send_message(chat_id,'Cep não encontrado')

def responder(cep):
    bot.send_message(chat_id,f'{cep["logradouro"]}, {cep["bairro"]}, {cep["localidade"]}, {cep["uf"]}')

bot.polling()









