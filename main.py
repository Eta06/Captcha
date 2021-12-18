#   Importing required libraries
from captcha.image import ImageCaptcha
#   We define the dimensions of the image we want to be created.
image = ImageCaptcha(width= 280, height= 90)
#   We define the text that will be created on the captcha.
captcha_text = 'Love'

data = image.generate(captcha_text)
#   We define the name of the created png file
image.write(captcha_text, 'CAPTCHA.png')