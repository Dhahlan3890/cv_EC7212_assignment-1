import cv2
import matplotlib.pyplot as plt

def apply_mean_filter(image, kernel_size):

    return cv2.blur(image, (kernel_size, kernel_size))

def main():

    image_path = input("Enter image path: ")
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found.")
        return

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    avg_3 = apply_mean_filter(gray_img, 3)
    avg_10 = apply_mean_filter(gray_img, 10)
    avg_20 = apply_mean_filter(gray_img, 20)

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.title("Original Image")
    plt.imshow(gray_img, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title("3x3 Averaging")
    plt.imshow(avg_3, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title("10x10 Averaging")
    plt.imshow(avg_10, cmap='gray')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title("20x20 Averaging")
    plt.imshow(avg_20, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
