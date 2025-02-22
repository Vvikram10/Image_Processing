from PIL import Image,ImageFilter


img = Image.open('dog.jpeg')
print(img.format) #JPEG
print(img.mode) #RGB

filter_img = img.filter(ImageFilter.BLUR)
filter_img.save('dog_blur.png','png') # creating blur images

filter_img = img.filter(ImageFilter.SMOOTH)
filter_img.save('dog_smooth.jpeg','jpeg') # creating smooth images

filter_img = img.filter(ImageFilter.SHARPEN)
filter_img.save('dog_sharpen.png','png') # creating smooth images

filter_img = img.convert('L') # use for grey scale conversion
filter_img.save('grey.png','png')