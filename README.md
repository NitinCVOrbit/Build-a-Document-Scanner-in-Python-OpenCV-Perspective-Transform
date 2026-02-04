# 📄 Document Scanner using OpenCV (Perspective Transform)

This project is a **Python-based Document Scanner** that converts a tilted or skewed document image into a clean, top-down scanned version using **Perspective Transformation** and **Adaptive Thresholding**.

It demonstrates real-world **Computer Vision** techniques used in mobile scanner apps.

---

## 🚀 Features

- Select document corners using **mouse clicks**
- Straighten document using **Perspective Transform**
- Convert image to grayscale
- Apply **Adaptive Thresholding** for scan-like output
- Interactive OpenCV window

---

## 🧠 Concepts Used

- Perspective Transformation (Homography)
- Image Warping
- Mouse Events in OpenCV
- Grayscale Processing
- Adaptive Thresholding

---

## 🛠 Tech Stack

- Python  
- OpenCV  
- NumPy  

---

## 📂 Project Workflow

1. Load the input image  
2. Click 4 document corner points (TL → TR → BR → BL)  
3. Compute transformation matrix  
4. Warp image to top view  
5. Convert to grayscale  
6. Apply adaptive threshold  
7. Display scanned output  

---
