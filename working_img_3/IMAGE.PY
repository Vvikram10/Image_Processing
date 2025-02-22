from PIL import Image,ImageFilter
img = Image.open('OIP.jpeg')
res = img.resize((500,500))
res.save('big.png','png')
# if You want to reduce size  and not want to crop image use thumnail
# its heplful when You need to reduce size for social media platform small size image
img.thumbnail((200,200)) # thumnail not return any image so we cant store it (w,H)
img.save('thumb.png','png')


