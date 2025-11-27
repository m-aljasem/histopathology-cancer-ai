"""
Training script for histopathology cancer detection.
"""

import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
import numpy as np
import cv2
import os
from pathlib import Path

from model import build_cnn_model


def load_images(image_paths, labels, target_size=(50, 50)):
    """Load and preprocess images."""
    images = []
    for path in image_paths:
        img = cv2.imread(path)
        img = cv2.resize(img, target_size)
        images.append(img)
    return np.array(images) / 255.0


def train_model(data_path='../data', epochs=40, batch_size=35):
    """Main training function."""
    print("Training histopathology cancer detection model...")
    
    # Load data - adjust paths based on your structure
    # X, y = load_your_data()
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Build model
    model = build_cnn_model(input_shape=(50, 50, 3))
    
    # Callbacks
    callbacks = [
        EarlyStopping(monitor='val_loss', patience=5),
        ModelCheckpoint('../models/histopathology_model.h5', save_best_only=True)
    ]
    
    # Train
    # history = model.fit(X_train, y_train, validation_data=(X_test, y_test), 
    #                    epochs=epochs, batch_size=batch_size, callbacks=callbacks)
    
    print("Training complete!")


if __name__ == '__main__':
    train_model()

