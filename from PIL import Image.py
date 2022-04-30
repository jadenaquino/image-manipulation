from PIL import Image, ImageFilter
import os


size_300 = (300,300)
size_700 = (700,700)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn, fext))
        

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))


image1 = Image.open('one piece flag.jpeg')
image1.save('one piece flag.jpeg')


image1 = Image.open('evangelion.jpeg')
image1.save('evangelion.jpeg')

image1 = Image.open('smash bros.jpeg')
image1.convert(mode=L).save('smash bros.jpeg')

image1 = Image.open('cowboy bebop.jpeg')
image1.save('cowboy bebop.jpeg')

image1 = Image.open('cup_game.jpeg')
image1.filter(ImageFilter.GuassianBlur(10)).save('cup_game.jpeg')

image1 = Image.open('dark souls.jpeg')
image1.rotate(45).save('dark souls.jpeg')

image1 = Image.open('kermit.jpeg')
image1.save('kermit.jpeg')

image1 = Image.open('metal gear rising.jpeg')
image1.save('metal gear rising.jpeg')

image1 = Image.open('guts.jpeg')
image1.save('guts.jpeg')

image1 = Image.open('el psy congro.jpeg')
image1.save('el psy congro.jpeg')