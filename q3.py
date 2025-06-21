import cv2
import numpy as np
import matplotlib.pyplot as plt

def rotate_image(image, angle):
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)

    cos = np.abs(rot_mat[0, 0])
    sin = np.abs(rot_mat[0, 1])
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    rot_mat[0, 2] += (new_w / 2) - center[0]
    rot_mat[1, 2] += (new_h / 2) - center[1]

    rotated = cv2.warpAffine(image, rot_mat, (new_w, new_h), flags=cv2.INTER_LINEAR)
    return rotated

def main():

    image_path = input("Enter image path: ")
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found.")
        return

    rot_45 = rotate_image(img, 45)
    rot_90 = rotate_image(img, 90)

    plt.figure(figsize=(10, 6))

    plt.subplot(1, 3, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Rotated 45°")
    plt.imshow(cv2.cvtColor(rot_45, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("Rotated 90°")
    plt.imshow(cv2.cvtColor(rot_90, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
