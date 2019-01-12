import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

now = datetime.datetime.now()


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 50) # GPIO 17 for PWM with 50Hz

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Received: %s' % command)

    if command == 'abrir':
        telegram_bot.sendMessage (chat_id, str("Abrindo"))
        p.start(3.5) # Initialization
        #p.ChangeDutyCycle(4.5)    #Enviamos uma pressão de 4.5% para rodar o servo para a esquerda
    elif command == 'fechar':
        telegram_bot.sendMessage (chat_id, str("fechando"))
        p.ChangeDutyCycle(11.5)   #Enviamos uma pressão de 10.5% para rodar o servo para a direita
    elif command == 'centralizar':
        telegram_bot.sendMessage (chat_id, str("centralizando"))
        p.ChangeDutyCycle(7.5)    #Enviamos uma pressão de 7.5% para centrar o servo de novo
    elif command == 'desligar':
        telegram_bot.sendMessage (chat_id, str("desligando"))
        p.stop()                      
telegram_bot = telepot.Bot('762116557:AAF6pleFdhAmaDIDaz4u4dFEIxebbPTFkd4')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Rodando...')

while 1:
    time.sleep(10)
