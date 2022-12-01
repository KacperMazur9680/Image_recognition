from PIL import Image
from matplotlib import pyplot
from numpy import asarray

image = Image.open("image_prep/The-Sydney-Harbor-Bridge.jpg")

pixels = asarray(image)
print(f"Data type: {pixels.dtype}")
print(f"Min: {pixels.min()} Max: {pixels.max()}")

pixels = pixels.astype("float32")

pixels /= 255.0
print(f"Min: {pixels.min()} Max: {pixels.max()}")

print("----------------------------------------------------------------\n") 
# global centering pixel values

pixels = asarray(image)
pixels = pixels.astype("float32")

mean = pixels.mean()
print("Mean: ", mean)
print(f"Min: {pixels.min()} Max: {pixels.max()}")

pixels = pixels - mean
mean = pixels.mean()

print("Mean: %.3f" % mean)
print("Min: %.3f  Max: %.3f" % (pixels.min(), pixels.max()))

print("----------------------------------------------------------------\n") 
# local centering pixel values

pixels = asarray(image)
pixels = pixels.astype("float32")

means = pixels.mean(axis=(0,1), dtype="float64")
print("Means: %s" % means)
print(f"Mins: {pixels.min(axis=(0,1))} Max: {pixels.max(axis=(0,1))}")

pixels -= means
means = pixels.mean(axis=(0,1), dtype="float64")
print("Means: %s" % means)
print(f"Mins: {pixels.min(axis=(0,1))} Max: {pixels.max(axis=(0,1))}")

print("----------------------------------------------------------------\n") 
# per channel pixel standardization

pixels = asarray(image)

pixels = pixels.astype("float32")

means = pixels.mean(axis=(0,1), dtype="float64")
stds = pixels.std(axis=(0,1), dtype="float64")
print("Means: %s, Stds: %s" % (means, stds))
pixels = (pixels - means) / stds

means = pixels.mean(axis=(0,1), dtype="float64")
stds = pixels.std(axis=(0,1), dtype="float64")
print("Means: %s, Stds: %s" % (means, stds))