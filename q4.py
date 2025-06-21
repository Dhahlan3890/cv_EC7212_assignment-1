import cv2
import numpy as np
import matplotlib.pyplot as plt

def block_average(image, block_size):

    h, w = image.shape
    output = image.copy()

    for i in range(0, h - block_size + 1, block_size):
        for j in range(0, w - block_size + 1, block_size):
            block = image[i:i + block_size, j:j + block_size]
            avg_val = np.mean(block, dtype=np.float32)
            output[i:i + block_size, j:j + block_size] = int(avg_val)

    return output

def main():

    image_path = input("Enter image path: ")
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found.")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    avg_3 = block_average(gray, 3)
    avg_5 = block_average(gray, 5)
    avg_7 = block_average(gray, 7)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.title("Original")
    plt.imshow(gray, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title("3x3 Block Averaging")
    plt.imshow(avg_3, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title("5x5 Block Averaging")
    plt.imshow(avg_5, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title("7x7 Block Averaging")
    plt.imshow(avg_7, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
