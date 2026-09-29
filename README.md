# Object Detection and Tracking using YOLO

A computer vision project that detects and tracks objects in video using YOLO11, OpenCV, and ByteTrack.

## 📌 Project Overview

Object detection and tracking are important applications of computer vision used in areas such as surveillance, traffic monitoring, robotics, security systems, and video analytics.

This project implements an object detection and tracking system using a pre-trained YOLO11 model.

The system processes a video frame by frame, detects objects, draws bounding boxes, displays object names and confidence scores, and assigns tracking IDs to detected objects.

---

## ✨ Features

- 🎯 Object detection using YOLO11
- 🔍 Object tracking using ByteTrack
- 📦 Bounding boxes around detected objects
- 🏷️ Object labels
- 📊 Confidence scores
- 🆔 Tracking IDs
- 🎥 Video processing using OpenCV
- ⚡ Frame-by-frame detection and tracking
- 🖥️ Real-time visualization of results

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| YOLO11 | Object detection |
| Ultralytics | YOLO implementation |
| OpenCV | Video processing |
| PyTorch | Deep learning framework |
| ByteTrack | Object tracking |

---

## 🧠 System Workflow

```text
Input Video
     ↓
OpenCV Video Capture
     ↓
Read Video Frame
     ↓
YOLO11 Object Detection
     ↓
ByteTrack Object Tracking
     ↓
Bounding Boxes + Labels + Tracking IDs
     ↓
Display Output
