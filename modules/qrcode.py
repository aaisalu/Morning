from amzqr import amzqr
import os

def folder(file):
    global Path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    Path=rf"{desktop}\{file}"
    if not os.path.exists(Path):
        os.makedirs(Path)
    return Path

version, level, qr_name = amzqr.run(
    'hello',
    version=20,
    level='Q',
    picture=r'C:\\Users\\helo\Desktop\\Morning\\Morning\\modules\\onelove.jpg',
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name='hello.png',
    save_dir=folder("qrcode")

)