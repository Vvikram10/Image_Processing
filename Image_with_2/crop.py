# let say i want to crop image its basic here for more you can visit documentation

from PIL import Image,ImageFilter
img = Image.open('grey.png')
filter_img = img.convert('L')
box = (100, 100, 200, 200) # four corner (left, upper, right, lower)
regine = filter_img.crop(box)
regine.save('regin.png','png')
