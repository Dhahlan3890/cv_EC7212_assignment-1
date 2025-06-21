import cv2
import numpy as np
import matplotlib.pyplot as plt

def reduce_intensity_levels(image, levels):

    if levels < 2 or levels > 256 or (levels & (levels - 1)) != 0:
        raise ValueError("Levels must be a power of 2 between 2 and 256")

    interval = 256 // levels

    reduced_img = (image // interval) * interval

    return reduced_img.astype(np.uint8)

def main():

    image_path = input("Enter path to image: ")
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found.")
        return

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    try:
        levels = int(input("Enter number of intensity levels (power of 2, e.g., 2, 4, 8, ... 256): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    try:
        reduced_img = reduce_intensity_levels(gray_img, levels)
    except ValueError as e:
        print(e)
        return

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(gray_img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title(f"Reduced to {levels} levels")
    plt.imshow(reduced_img, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
