from keras.utils import load_img, array_to_img, img_to_array, save_img
from matplotlib import pyplot

img = load_img("image_prep/The-Sydney-Harbor-Bridge.jpg")

print(type(img))

img_ar = img_to_array(img)
print(img_ar.dtype)
print(img_ar.shape)

ar_img = array_to_img(img)
print(type(ar_img))

img_gray = load_img("image_prep/The-Sydney-Harbor-Bridge.jpg", color_mode="grayscale")
img_gray_array = img_to_array(img_gray)
save_img("image_prep/The-Sydney-Harbor-Bridge-Gray.jpg", img_gray_array)

img_g = load_img("image_prep/The-Sydney-Harbor-Bridge-Gray.jpg")

