from rembg import remove
import cv2 as cv


# path of input image
input_path = 'image.jpg'


# path for saving output image
output_path = 'output.jpg'

# reading the image
input_image = cv.imread(input_path)

# output
output = remove(input_image)

cv.imwrite(output_path, output)