from PIL import Image,ImageFilter

img = Image.open('grey.png')
filter_img = img.convert('L')
res = filter_img.resize(300,300) # resize actual size is 474 X 266 i want to 300 X 300 but make sure resize need tuple otherwise it get error
'''
when you not pass resize value inside tuple


Traceback (most recent call last):
  File "C:\Users\vikram\Desktop\Leaarn_new\Image_with_2\image.py", line 7, in <module>
    res = filter_img.resize(300,300) # resize actual size is 474 X 266 i want to 300 X 300 but make sure resize need tuple otherwise it get error
  File "C:\Users\vikram\AppData\Roaming\Python\Python310\site-packages\PIL\Image.py", line 2315, in resize
    raise ValueError(msg)
ValueError: Unknown resampling filter (300). Use Image.Resampling.NEAREST (0), Image.Resampling.LANCZOS (1), Image.Resampling.BILINEAR (2), Image.Resampling.BICUBIC (3), Image.Resampling.BOX (4) or Image.Resampling.HAMMING (5)
'''
res = filter_img.resize((300,300)) # here i pass values inside tuple
res.save('resize.png','png') 
