#!/usr/bin/env python3
import numpy as np
import cv2  # pip install opencv-python
import os
import random
import pickle  # To save and load serialized data

# Define constants
DIRECTORY = r'c:/Users/anjala/Documents/dataset'  # Your dataset path
CATEGORIES = ['Cats', 'Dogs']
IMG_SIZE = 100

def create_dataset():
    data = []

    for category in CATEGORIES:
        path = os.path.join(DIRECTORY, category)
        class_num = CATEGORIES.index(category)  # 0 for Cats, 1 for Dogs

        for img in os.listdir(path):
            try:
                img_path = os.path.join(path, img)
                img_arr = cv2.imread(img_path)  # Read the image
                img_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))  # Resize the image
                data.append([img_arr, class_num]) 
            except Exception as e:
                print(f"Error processing {img_path}: {e}")

    random.shuffle(data)  # Shuffle the data for better training

    # Separate features (images) and labels
    X = []
    y = []
    for features, label in data:
        X.append(features)
        y.append(label)

    X = np.array(X)
    y = np.array(y)

    # Save the data to files
    pickle.dump(X, open('X.pkl', 'wb'))
    pickle.dump(y, open('y.pkl', 'wb'))

    print("Dataset created and saved successfully.")

if __name__ == "__main__":
    create_dataset()