from numpy import argmax
from keras.utils import img_to_array
from keras.models import load_model
import cv2
 
# load and prepare the image
def load_image(filename):
    # load the image
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28,28))
    img_invrt = cv2.bitwise_not(image)
    # convert to array
    img = img_to_array(img_invrt)
    # reshape into a single sample with 1 channel
    img = img.reshape(1, 28, 28, 1)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img
 
# load an image and predict the class
def run_example():
 # load the image
 img = load_image('Project_1_digit/sample_image.jpg')
 # load model
 model = load_model('Project_1_digit/digit_model.h5')
 # predict the class
 predict_value = model.predict(img)
 digit = argmax(predict_value)
 print(digit)
 
# entry point, run the example
run_example()