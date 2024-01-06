from remove_background import *
from place_logo_on_mockup import *

mockup2 = {'path': r'mock\2\mockup.jpg', 'boxsize': (800,800), 'boxanker':(1050,350),'mid_point': (1050+800//2,350+800//2)}

logo_num = input("logo number: \n")

logo = fr'logo\after\logo{logo_num}.png'

out_num = input("out number: \n")
out1 = fr'out\{out_num}.jpg'



remove_background2(fr'logo\before\logo{logo_num}.jpeg',logo)
remove_watermark(logo,fr'logo\no_watermark\logo{logo_num}.png')
use_mockup2(fr'logo\no_watermark\logo{logo_num}.png',mockup2,out1,size = 600)





