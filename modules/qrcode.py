from amzqr import amzqr
import os,re,glob

def folder(file):
    global Path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    Path=rf"{desktop}\{file}"
    if not os.path.exists(Path):
        os.makedirs(Path)
    return Path

def chkreg(answer):
    return re.search("yes|1|yep|sure|True|yess|hellyeah|yeah",f'{answer}',flags=re.IGNORECASE)  

def getimg(string):
    path=r'..\gallery'
    if os.path.isdir(path):
        for k in glob.glob(rf'{path}\*.{string}'):
            return k,f'{string}'
    else:
       print("Gallery folder can't be found in the Morning project folder")
       return None,'png'


def roulette(info):
    askimg=input("Do you want custom img or gif as output? [yes/no]: ")
    try:
        if chkreg(askimg):
            asktype=input("Do you want gif as output? [yes/no]: ")
            if chkreg(asktype):
                if not None is (storegif:=getimg('gif')):
                    print("\nProcessing output as gif with custom img.")
                    return engine(info,storegif[0],storegif[1],True,10)                         
                else:
                    print("GIF isn't present in gallery folder so, processing output with jpg.") 
                    return engine(info,None,'jpg',True,7) 
            else:
                if not None is (storeimg:=getimg('jpg')):
                    print("\nProcessing output as png with custom img.")
                    return engine(info,storeimg[0],storeimg[1],True,10)                         
                else:
                    print("Picture isn't present in gallery folder so, processing output with png.") 
                    return engine(info,None,'png',True,7) 
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
    contrast=1.2,
    brightness=1.1,
    save_name=f'{info[:10]}.{ext}',
    save_dir=folder("Qrcodes"))

roulette(str(input("Type anything which you want to convert it to QRcode: ")))               
