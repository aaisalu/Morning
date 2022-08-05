from amzqr import amzqr
import os,re

def folder(file):
    global Path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    Path=rf"{desktop}\{file}"
    if not os.path.exists(Path):
        os.makedirs(Path)
    return Path

def chkreg(answer):
    return re.search("yes|1|yep|sure|True|yess|hellyeah|yeah",f'{answer}',flags=re.IGNORECASE)  

def roulette(info):
    askimg=input("Do you want custom img or gif as output? [yes/no]: ")
    if chkreg(askimg):
        asktype=input("Do you want gif as output? [yes/no]: ")
        if chkreg(asktype):
            print("Processing output as gif with custom img")
            return engine(info,r'..\images\rickroll.gif','gif',True)  
        else:
            print("Processing output as png with custom img")
            return engine(info,r'..\images\onelove.jpg','png',True)
    else:
        print("Processing output as jpg without any custom img")
        return engine(info,None,'jpg',True)

def engine(info,img,ext,color):
    version, level, qr_name = amzqr.run(
    info,
    version=10,
    level='Q',
    picture=img,
    colorized=color,
    contrast=1.0,
    brightness=1.0,
    save_name=f'{info[:10]}.{ext}',
    save_dir=folder("Qrcodes"))

roulette(str(input("Type anything which you want to convert it to QRcode: ")))               


