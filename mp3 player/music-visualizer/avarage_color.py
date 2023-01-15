from PIL import Image, ImageStat

def avrg_clr(filename):

    img = Image.open(filename)
    mean = ImageStat.Stat(img).mean
    color = '{:.0f} {:.0f} {:.0f}'.format(*mean)

    return color.split(' ')


