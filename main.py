import time
import sys
from instabot import Bot
import os
hashtags = ""
from win10toast import ToastNotifier
from datetime import date, datetime

def execute():
    # path to file with the number of the last photo uploaded, max is 50
    f=open("n.txt", "r")
    n = f.readline()
    f.close()
    n = int(n)
    l = n
    n = str(n)
    # path to file with the captions for each  patricular photo
    with open("captions.txt") as fp:
        for i, line in enumerate(fp):
            if i == l-1:
                s=line
            elif i > 50:
                toaster = ToastNotifier()
                toaster.show_toast("Reload photos","n>50")
                sys.exit()

    
    arr = os.listdir("folder") # the folder with photos
    bot = Bot()
    bot.login(username = "your_username",password = "your_password")
    bot.upload_photo("folder" + n +".jpg", caption = caption + hashtags ) # n is the number of photo to be uploaded
    n=int(n)
    if (n<50):
        n=n+1
    elif (n==50):
        n=1
    n = str(n)
    file = open("n.txt","w") # modify n if photo is uploaded
    file.write(n)
    file.close()
    toaster = ToastNotifier()
    toaster.show_toast("Succes","photo uploaded")




today = date.today()
today=str(today)

epoch = os.path.getmtime('date.txt') # in this file we keep the last date when a photo was uploaded

md = time.strftime('%Y-%m-%d',time.localtime(epoch))


if today==md: # per day you can post only 1 photo
    toaster = ToastNotifier()
    toaster.show_toast("Photo already uploaded ","------------------")
else:
    print('y')
    execute()
    with open('date.txt','w+') as f:
        f.write('m')
