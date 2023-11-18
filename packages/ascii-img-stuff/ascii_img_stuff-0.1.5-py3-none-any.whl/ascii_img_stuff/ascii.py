#!/usr/bin/python3
# https://github.com/hashirkz/ascii_stuff

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mimg
import os
import logging as log
from skimage.transform import resize

# logfile setup stuff
log.basicConfig(filename='error.log', level=log.ERROR)

# normalize and invert np.ndarray 
norm = lambda x : (x-np.min(x))/(np.max(x)-np.min(x))
invert = lambda x : 1.0 - x

# utility grayscale rbg m x n x 3 tensors to m x n 
def rgb2gray(rgb: np.ndarray) -> np.ndarray:
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

# utility rescale img and crop img to square *same aspect ratio
# default 128 h 
# the aspect ratio of the terminal in ascii characters i around 0.5/0.2 *2.5 so w is scaled up by that amt to counteract this
def rescale(img: np.ndarray, h=32) -> np.ndarray:

    # grayscale imgs rescale
    if len(img.shape) == 2:
        row, col = img.shape
        asp = row / col
        w = int(h * 2.5 / asp)
        resized = resize(img, (h, w))
        return resized

    # color img rescale
    elif len(img.shape) == 3:
        pass


# read image data into numpy array 
def read_img(path: str, show=False, save=False, inv=True) -> np.ndarray:
    try:
        img = plt.imread(path)
        img = norm(img)
        if inv: img = invert(img)
        img = rgb2gray(img)

        # show img attributes
        if show:
            row, col = img.shape
            print(f'dimensions: {row} x {col}')

        # save img 
        if save:
            plt.imsave(f'1_{os.path.basename(path)}', img, format='png', cmap='gray')

        return img
    except FileNotFoundError as err:
        log.error(f'ERROR: {err}, msg: unable to find {path} in {os.getcwd()}')
        return 

# image to ascii characters
# bins from [1/len(chset), 1, len(chset)+2] so lowest bin is white space
# change to [0, 1, len(chset)+1] if . for whitespace
def img_to_ascii(img: np.ndarray, show=False, chset=' .:-=+*#%@') -> np.ndarray:
    # grayscale ascii character ramp/map
    bins = np.linspace(1/len(chset), 1, len(chset))
    ascii = [ch for ch in chset]
    
    mapped = np.digitize(img, bins)
    mapped = np.vectorize(ascii.__getitem__)(mapped)
    return mapped

# pretty print ascii img to console
def pretty_repr(img: np.ndarray, show=True, save=False, savepath: str=None) -> str:
    repr = ''
    for row in img:
        for col in row:
            repr += col
        repr += '\n'
    
    if show: print(repr)
    if save: 
        with open(savepath, 'w') as file:
            file.write(repr)

    return repr

if __name__ == '__main__':
    pass

    

