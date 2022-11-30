from PIL import Image
from numpy import asarray
image = Image.open("image_prep/Sydney-Opera-House.jpg")

# print(image.format)
# print(image.mode)
# print(image.size)

# image.show()

# Diffrent approach
# from matplotlib import image, pyplot

# data = image.imread('image_prep/Sydney-Opera-House.jpg')
# print(data.dtype)
# print(data.shape)

# pyplot.imshow(data)
# pyplot.show()

data = asarray(image)
print(data.shape)

image2 = Image.fromarray(data)
print(image2.format)
print(image2.mode)
print(image2.size)

gr_scale = image2.convert(mode="L")
gr_scale.save("image_prep/Sydney_Opera_House_Gray.jpg")

image_gray = Image.open("image_prep/Sydney_Opera_House_Gray.jpg")
# image_gray.show()

print(image_gray.size)
image_gray.thumbnail((100,100))
print(image_gray.size)

image_gray.show()

image_gray2 = Image.open("image_prep/Sydney_Opera_House_Gray.jpg")

print(image_gray2.size)
image_gray2 = image_gray2.resize((100,100))
print(image_gray2.size)

image_gray2.show()