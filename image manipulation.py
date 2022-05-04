from PIL import Image, ImageFilter
import os

#the specific sizes on the main folder
size_300 = (300, 300)
size_450 = (450, 450)
size_650 = (650, 650)

#asking the user what image they want to show and then modify
while True:
    user_choice = input("what image would you like modify? (cowboy bebop, cuphead, dark souls, el psy congroo, evangelion, gurren lagann, guts, metal gear, straw hats flag, super smash bros) ")
    usershow =Image.open(user_choice + ".jpeg")
    usershow.show
    user_confirmation =input("Is this the correct image? (yes/no) ")
    if user_confirmation == "yes":
        break

choice = input("Pick your modifications (resize, png, black/white, blur, or rotate) ")


#rotate
if choice == "rotate":
    image1 = Image.open(user_choice + ".jpeg")
    image1.rotate(180).save('rotate/'+user_choice+'_rotate.jpeg')
    image2 = Image.open('rotate/'+user_choice+'_rotate.jpeg')
    image2.show()


#png
if choice == "png":
    image1 = Image.open(user_choice + ".jpeg")
    image1.save('png/'+user_choice+'.png')
    image2 = Image.open('png/'+user_choice+'.png')
    image2.show()

#blur
if choice == "blur":
    image1 = Image.open(user_choice + ".jpeg")
    image1.filter(ImageFilter.GaussianBlur(3)).save('blur/'+user_choice+'_blur.jpeg')
    image2 = Image.open('blur/'+user_choice+'_blur.jpeg')
    image2.show()


#black/white
if choice == "black/white":
    image1 = Image.open(user_choice + ".jpeg")
    image1.convert(mode='L').save('black and white/'+user_choice+'_black and white.jpeg')
    image2 = Image.open('black and white/'+user_choice+'_black and white.jpeg')
    image2.show()


#resize
if choice == "resize":
    #Open image.
    img1 = Image.open(user_choice + ".jpeg")
    #Print size
    print(img1.size)

    #Ask user for first input.
    #Ask user for second input.
    x = int(input("Enter size 1: "))
    y = int(input("Enter size 2: "))
    new_size = img1.resize((x, y))
    new_size.show()

    if x and y == 300:
        new_size.save("300/" + user_choice + ".jpeg")
    elif x and y == 450:
         new_size.save("450/" + user_choice + ".jpeg")
    elif x and y == 650:
         new_size.save("650/" + user_choice + ".jpeg")
    else:
         new_size.save("other_size/" + user_choice + ".jpeg")
    
    '''
    image1.save('300/'+user_choice+'_300.jpeg')
    image2 = Image.open('300/'+user_choice+'_300.jpeg')
    image2.show()
    
    '''
    






