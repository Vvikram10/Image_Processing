from PIL import Image,ImageFilter

img = Image.open('grey.png')
filter_img = img.convert('L')
# rot = filter_img.rotate(180) #  use for rotation
rot = filter_img.rotate(90)
rot.save('grey2.png','png') 