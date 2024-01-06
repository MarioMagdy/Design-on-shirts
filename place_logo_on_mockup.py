# import sys

# caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.insert(1, r'G:\pythoncodenew\remove_background')
# from remove_background import remove_background2
# remove_background = remove_background2

# logo1 = r'logo\after\logo1.png'
# remove_background(r'logo\before\logo1.jpeg',logo1)


# anker = (1050,350)
# size = 900
# mockup1 = {'path': r'mock\1\mockup.jpg', 'boxsize': (size,size), 'boxanker':(anker,anker),'mid_point': (anker[0]+size//2,anker[1]+size//2)}

# # mockup1 = 
# out1 = r'out\1.jpg'


# import module
from PIL import Image


def use_mockup2(logo,mockup,out,size=None):
    """Places the logo on the mockup, 
    and save it to out, you can opptionaly give it size parameter
    that allows you to scale the logo around the mid point of the box of the mockup"""
    # load images
    image = Image.open(logo)
    background = Image.open(mockup['path'])
    # print(back_np)

    if size is None:
        size = mockup['boxsize'][0]

    # resize image to 700x700
    image = image.resize((size,size))

    # paste image on background at position 320, 330
    background.paste(image, [i-size//2 for i in mockup['mid_point']],image)

    # save result as new image

    background.save(out)

# use_mockup2(logo1,mockup1,out1)