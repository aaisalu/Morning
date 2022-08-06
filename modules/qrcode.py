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
    try:
        if chkreg(askimg):
            asktype=input("Do you want gif as output? [yes/no]: ")
            if chkreg(asktype):
                print("\nProcessing output as gif with custom img")
                return engine(info,r'..\images\rickroll.gif','gif',True,10)  
            else:
                print("\nProcessing output as png with custom gif")
                return engine(info,r'..\images\onelove.jpg','png',True,10)
        else:
            print("Processing output as jpg without any custom img")
            return engine(info,None,'jpg',True,7)
    except ValueError:
        print("\nOh snap!! Feels like my brain can't process this input")
def engine(info,img,ext,color,ver):
    version, level, qr_name = amzqr.run(
    info,
    version=ver,
    level='Q',
    picture=img,
    colorized=color,
    contrast=1.0,
    brightness=1.0,
    save_name=f'{info[:10]}.{ext}',
    save_dir=folder("Qrcodes"))

roulette(str(input("Type anything which you want to convert it to QRcode: ")))               


