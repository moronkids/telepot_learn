import os
import datetime
import time
import telepot
import subprocess
import psutil
import sys
from telepot.loop import MessageLoop
from subprocess import Popen, PIPE

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Got command: %s' % command)
#start
    if command == '/start':
        z = "Available: \n\n /time \n /run \n /data \n /stat \n /bot_reboot \n\n Bot v1.0"
        bot.sendMessage(chat_id, z)

    if command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

    if command == '/run':
        output = ("Server is UP : ardani.serveo.net")
    	server = subprocess.call("", shell=True)
    	bot.sendMessage(chat_id, output)

    if command == '/data':
        trafik = subprocess.Popen(['ifconfig wlan0'], shell=True,
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
        out, err = trafik.communicate()
        #trafik = stdout.decode('utf-8')
	print(out)
        bot.sendMessage(chat_id, out)

    if command == '/stat':
        def allinone():
            #suhu-start
            suhu = os.popen('vcgencmd measure_temp').readline()
            #stop
            #RAM-start
            ram = os.popen('free')
            i = 0
            #stop
            #disk-start
            disk = os.popen("df -h /")
            o = 0
            #stop
            #masuk loop
            while 1:
                #loop-RAM-start
                i = i + 1
                line = ram.readline()
                lin= disk.readline()
                #stop
                #loop-disk-start
                o = o + 1

                if i==2 and o==2:
                    #kondisi-RAM-start
                    ram3 = (line.split()[3])
                    bg = (int(ram3))/1000
                    ram2=("RAM free: %s MB" % (str(bg)))

                    #stop
                    #kondisi-disk-start
                    total = (lin.split()[1])
                    usage = (lin.split()[2])
                    free = (lin.split()[3])
                    percentage = (lin.split()[4])
                    alli = ("Total : %s / Usage : %s / Free : %s / Percentage : %s" % (total, usage, free, percentage))

                    #stop
                    return("- %s \n- %s \n- %s" %(alli, ram2, suhu))
                    break
        bot.sendMessage(chat_id, allinone())


    if commaďnd == '/bot_reboot':
        ulang = subprocess.Popen(['python api.py'], shell=True)
        result= ("bot Telegram successful reboot !!")
        bot.sendMessage(chat_id, result)

    #stop
bot = telepot.Bot('548892113:AAEQ9eCkOaFsCSNQ6FpWHf92c_KmBwiN1CM')
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')
while 1:
    time.sleep(10)
