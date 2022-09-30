from turtle import color
import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

# find difference between two images
def find_difference(image1, image2):
    
    # check the simillarity between the shape of the images
    assert image1.shape == image2.shape, "Specify two image with the same shape."

    # convert entry images to gray scale
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)

    # find the metrics for the images
    # score (0 >= score >= 1): simillarity level between the images
    # difference_image: difference image between image1 and image2
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similarity of the images: ", score)
    
    # normalize difference image to enhace final result
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))

    return normalized_difference_image

# matche the histograms for the images
def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image