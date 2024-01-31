import cv2
import os
import glob
import numpy as np

def bounding_box_extraction(image_folder):
    # Iterate over all images in the folder
    for image_path in glob.glob(os.path.join(image_folder, '*.png')):
        # Load the grayscale mask image
        mask_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Check the loaded image
        if mask_image is None:
            print(f"Error: Unable to load the image {image_path}")
            continue

        # Threshold the image: Values greater than or equal to 1 become 255
        _, binary_mask = cv2.threshold(mask_image, 0.5, 255, cv2.THRESH_BINARY)

        # Find contours in the binary mask
        contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Output file details
        output_file_path = os.path.splitext(image_path)[0] + '.txt'

        # Write bounding box coordinates to the text file
        with open(output_file_path, 'w') as f:
            for contour in contours:
                flattened_contour = contour.reshape(-1, 2)  # Flatten the nested structure

                normalized_contour = (flattened_contour.astype(float) / np.array([mask_image.shape[1], mask_image.shape[0]])).tolist()

                # Write to the text file
                f.write("1")
                for point in normalized_contour:
                    f.write(" {} {}".format(point[0], point[1]))
                f.write("\n")

        # Deleting the image file
        os.remove(image_path)
                
#print("extracting bounding boxes for test...")
#bounding_box_extraction('./data/test/labels/', './data/test/bbox/')
#print("extracting bounding boxes for a test image")
#bounding_box_extraction('./test/', './test/')

#print("extracting bounding boxes for train...")
#bounding_box_extraction('./data/train/labels/', './data/train/bbox/')
#print("extracting bounding boxes for test...")
#bounding_box_extraction('./data/test/labels/', './data/test/bbox/')
#print("...finished extracting")

#print("extracting bounding boxes for train...")
#bounding_box_extraction('./git-repo/YOLOv8/datasets/data/train/labels', './git-repo/YOLOv8/datasets/data/train/bbox/')
#print("extracting bounding boxes for test...")
#bounding_box_extraction('./git-repo/YOLOv8/datasets/data/test/labels', './git-repo/YOLOv8/datasets/data/test/bbox/')
#print("...finished extracting")

print("extracting bounding boxes for train...")
bounding_box_extraction('./datasets/data/train/labels')
print("extracting bounding boxes for test...")
bounding_box_extraction('./datasets/data/test/labels')
print("...finished extracting")