# 🔬 Breast Histopathology Cancer Classification

Deep learning system for detecting **Invasive Ductal Carcinoma (IDC)** in breast histopathology patches.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13%2B-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-ff4b4b.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 👤 Author

- **Name**: Mohamad AlJasem, MD MPH MSc  
- **Email**: [mohamad@aljasem.eu.org](mailto:mohamad@aljasem.eu.org)  
- **GitHub**: [github.com/m-aljasem](https://github.com/m-aljasem)  
- **Website**: [aljasem.eu.org](https://aljasem.eu.org)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Model Architecture](#-model-architecture)
- [Exported Weights](#-exported-weights)
- [License](#-license)
- [Disclaimer](#-disclaimer)

---

## 🎯 Overview

This project implements a custom **CNN classifier** for breast histopathology images cropped into **50×50 patches**.  
The task is **binary classification**:

- **IDC (+)** – Invasive Ductal Carcinoma present  
- **IDC (−)** – No carcinoma

It builds on the popular Kaggle **“Breast Histopathology Images”** dataset and provides:

- A training pipeline
- Streamlit app for easy inference
- Exported model weights for deployment

---

## ✨ Features

- Custom multi-layer CNN tuned for small 50×50 patches
- Batch normalization and dropout for regularization
- Binary softmax output with confidence scores
- Streamlit UI to upload and classify patches

---

## 🛠 Tech Stack

- Python 3.8+
- TensorFlow / Keras
- Streamlit

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

Dev tools:

```bash
pip install -r requirements-dev.txt
```

---

## 🚀 Quick Start

### 1️⃣ Train the Model

```bash
cd breast-patho
python src/train.py
```

This will train the CNN and (once the data pipeline is wired) save:

```text
models/histopathology_model.h5
```

### 2️⃣ Run the Streamlit App

```bash
cd breast-patho
streamlit run app.py
```

Upload a 50×50 histopathology patch and view:
- Prediction: **IDC Present** or **No IDC**
- Confidence score

---

## 🧑‍💻 Usage

### 🌐 Web App

```bash
streamlit run app.py
```

The app:
- Builds the CNN model
- Loads weights from `models/histopathology_model.h5` if available
- Falls back to random weights (with a warning) if not trained yet

### 🧬 Programmatic Usage

```python
from src.model import build_cnn_model
import numpy as np

model = build_cnn_model()
model.load_weights("models/histopathology_model.h5")  # after training

# img: 50x50x3 numpy array, scaled to [0,1]
img_batch = np.expand_dims(img, 0)
pred = model.predict(img_batch, verbose=0)[0]
label = np.argmax(pred)
confidence = pred[label]
```

---

## 🗂 Project Structure

```text
breast-patho/
├── app.py                    # Streamlit app
├── config/
├── data/                     # Histopathology dataset (IDC_regular_ps50_idx5)
├── docs/
├── experiments/
├── models/                   # Saved weights (histopathology_model.h5)
├── notebooks/
├── scripts/
├── src/
│   ├── __init__.py
│   └── model.py              # build_cnn_model()
└── tests/
```

---

## 🧬 Dataset

- **Name**: Breast Histopathology Images (IDC_regular_ps50_idx5)  
- **Source**: Kaggle – paultimothymooney/breast-histopathology-images  
- **Resolution**: 50×50 pixel RGB patches  

Labels:

- `0` – **No IDC (Negative)**  
- `1` – **IDC Present (Positive)**  

---

## 🧱 Model Architecture

- Stacked `Conv2D` layers with ReLU activations
- `BatchNormalization` for stable training
- `MaxPooling2D` for downsampling
- Dense layers with dropout
- Final `Dense(2, activation="softmax")` for binary classification

Weights are exported as:

```text
models/histopathology_model.h5
```

---

## 📦 Exported Weights

- Training script saves to:

```text
../models/histopathology_model.h5
```

- Streamlit app loads from:

```text
models/histopathology_model.h5
```

You can copy the `models/` directory to any other environment and reuse the trained model.

---

## 📄 License

Licensed under the **MIT License**.  
See `LICENSE` for details.

---

## 🏥 Disclaimer

> This project is for **research and educational use only**.  
> It must **not** be used for clinical diagnosis or treatment decisions.

