from PIL import Image

imgwidth = 2497
imgheight = 3535

img = Image.open("temp.jpg")

img = img.resize((imgwidth,imgheight),Image.ANTIALIAS)

img.save("resizedImg.jpg")
