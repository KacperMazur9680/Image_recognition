from PIL import Image
from matplotlib import pyplot

image = Image.open("image_prep/Sydney-Opera-House.jpg")

horztl_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
vercl_flip = image.transpose(Image.FLIP_TOP_BOTTOM)

pyplot.subplot(531)
pyplot.imshow(image)
pyplot.subplot(532)
pyplot.imshow(horztl_flip)
pyplot.subplot(533)
pyplot.imshow(vercl_flip)
pyplot.subplot(537)
pyplot.imshow(image.rotate(45))
pyplot.subplot(538)
pyplot.imshow(image.rotate(90))

pyplot.show()

cropped = image.crop((100,100, 200, 200))
cropped.show()

