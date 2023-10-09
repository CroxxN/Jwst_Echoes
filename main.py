from util import *
from PIL import Image

image = Image.open('assets/demo2.jpg')
son = Sonify(image=image, soundfont_path='assets/Levi_s_Violin.sf2')
son.run()
