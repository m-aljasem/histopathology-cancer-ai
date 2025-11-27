"""CNN model for histopathology image classification"""
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam


def build_cnn_model(input_shape=(50, 50, 3)):
    """Build CNN for binary cancer classification."""
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=input_shape),
        BatchNormalization(),
        Conv2D(32, (3, 3), activation='relu', padding='same'),
        MaxPooling2D((2, 2)),
        BatchNormalization(),
        Dropout(0.3),
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        Conv2D(64, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Dropout(0.3),
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        Flatten(),
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dense(64, activation='relu'),
        BatchNormalization(),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(24, activation='relu'),
        Dense(2, activation='softmax')
    ])
    model.compile(Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])
    return model

