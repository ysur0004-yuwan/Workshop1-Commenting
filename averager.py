import numpy as np # imports a libary that does fast arrays of math 
from PIL import Image # allows opening and saving image files 
import os # work with file paths 
from glob import glob # find files matching a pattern 

def average_images(input_dir: str, output_path: str = "averaged.png"):
    # Collect every PNG file in the input directory.
    files = sorted(glob(os.path.join(input_dir, "*.png")))

    # Fail early if there are no images to combine.
    if not files:
        raise ValueError("No PNG images found in directory.")

    # Use the first image to establish the expected shape and channels.
    # float64 is used so repeated additions cannot overflow.
    first = np.array(Image.open(files[0]), dtype=np.float64)
    accumulator = np.zeros_like(first)

    # Add each image's pixels to the running total.
    for f in files:
        accumulator += np.array(Image.open(f), dtype=np.float64)

    # Divide total pixel values by number of images to get their mean.
    # Convert back to uint8 (standard 0–255 image data).
    averaged = (accumulator / len(files)).astype(np.uint8)

    # Convert the array back to an image and save it.
    Image.fromarray(averaged).save(output_path)
    print(f"Averaged image saved to {output_path}")
