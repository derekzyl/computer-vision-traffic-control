Here's a more robust and professional explanation of your project, incorporating the provided details and directory structure:

---

<div align="center">

# Smart Traffic Control System with Raspberry Pi, FastAPI, and YOLOv5

</div>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()  
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

<div align="center">

<img src="assets/output.gif" width="1000px" height="600px">

</div>

## Overview

The Smart Traffic Control System is an innovative solution designed to optimize traffic flow at intersections using video-based vehicle detection. This project integrates Raspberry Pi for edge video capture, FastAPI for backend processing, and YOLOv5 for object detection, enabling dynamic traffic light management based on real-time vehicle density.

### Key Features

- **Edge Video Capture:** Utilizes Raspberry Pi to capture short video snippets of each lane using an OpenCV-compatible webcam. The system employs a motor driver for accurate lane snapshots.
- **Backend Processing:** Captured videos are sent to a FastAPI server where they are processed using YOLOv5 for vehicle detection. The server calculates optimal green and red light durations for each lane based on the detected vehicle count.
- **Traffic Light Control:** The Raspberry Pi receives the computed timings and controls the traffic lights accordingly, incorporating a countdown timer for enhanced traffic management.

## System Workflow

1. **Video Capture:** Raspberry Pi captures short video feeds for each lane.
2. **Video Transmission:** The captured videos are transmitted to the server via FastAPI.
3. **Video Processing:** The server processes the videos using YOLOv5 to detect vehicles and determine the vehicle count in each lane.
4. **Traffic Timing Calculation:** Based on the vehicle count, the system calculates the optimal green and red light durations for the X and Y lanes.
5. **Traffic Light Control:** The Raspberry Pi controls the traffic lights using the calculated durations, with a real-time countdown display.

### Example Output
The system returns the following data structure, where `x1_vehicles`, `x2_vehicles`, `y1_vehicles`, and `y2_vehicles` represent vehicle counts in the respective lanes, and `x_green_time` and `y_green_time` represent the green light durations:

```json
{
  "id": "20240413060929emkax651ip2ff3e1acea50443b9b6ed854613634e6",
  "x1_vehicles": 0,
  "x2_vehicles": 0,
  "y1_vehicles": 0,
  "y2_vehicles": 0,
  "x_green_time": 60,
  "y_green_time": 60
}
```

## Project Structure

The project is organized as follows:

```
project
├── LICENSE
├── README.md
├── assets
│   └── output.gif
├── config  # Configuration files for the project
│   └── ... (other config-related files)
├── deep_sort  # Deep Sort tracking implementation
│   ├── configs  # Config files for Deep Sort
│   ├── deep  # Deep learning-related code
│   ├── sort  # Sorting algorithm implementation
│   ├── utils  # Utility scripts for Deep Sort
│   ├── deep_sort.py  # Main Deep Sort script
│   └── __init__.py  # Initialization script
├── module  # Custom modules for the project
│   └── __pycache__  # Compiled Python files
├── traffic  # Traffic light control logic
│   ├── controller.py  # Main controller for traffic light logic
│   ├── model.py  # Models for traffic data
│   ├── service.py  # Services for processing and logic
│   ├── __init__.py  # Initialization script
├── uploads  # Directory for video uploads from Raspberry Pi
│   └── ... (sample videos for testing)
├── yolov5  # YOLOv5 model integration
│   ├── classify  # YOLOv5 classification scripts
│   ├── data  # Data handling scripts for YOLOv5
│   ├── models  # YOLOv5 models
│   ├── segment  # Segmentation models and scripts
│   ├── utils  # Utility scripts for YOLOv5
│   ├── detect.py  # Object detection script using YOLOv5
│   ├── export.py  # Script for exporting models
│   ├── train.py  # Script for training YOLOv5 models
│   ├── hubconf.py  # Hub configuration for YOLOv5
│   ├── requirements.txt  # Python dependencies for YOLOv5
│   └── ... (other YOLOv5 related files)
└── yolov5s.pt  # YOLOv5 model weights file
```

## Setup Instructions

### 1. Clone the YOLOv5 Repository
```bash
git clone https://github.com/ultralytics/yolov5.git
```

### 2. Install Required Dependencies
Install the necessary libraries for both the YOLOv5 and FastAPI components:
```bash
pip install -r requirements.txt && cd yolov5 && pip install -r requirements.txt
```

### 3. Run the FastAPI Server
Start the server using:
```bash
uvicorn main:app --reload
```
Here's a more robust and professional explanation of your project, incorporating the provided details and directory structure:

---

<div align="center">

# Smart Traffic Control System with Raspberry Pi, FastAPI, and YOLOv5

</div>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()  
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

<div align="center">

<img src="assets/output.gif" width="1000px" height="600px">

</div>

## Overview

The Smart Traffic Control System is an innovative solution designed to optimize traffic flow at intersections using video-based vehicle detection. This project integrates Raspberry Pi for edge video capture, FastAPI for backend processing, and YOLOv5 for object detection, enabling dynamic traffic light management based on real-time vehicle density.

### Key Features

- **Edge Video Capture:** Utilizes Raspberry Pi to capture short video snippets of each lane using an OpenCV-compatible webcam. The system employs a motor driver for accurate lane snapshots.
- **Backend Processing:** Captured videos are sent to a FastAPI server where they are processed using YOLOv5 for vehicle detection. The server calculates optimal green and red light durations for each lane based on the detected vehicle count.
- **Traffic Light Control:** The Raspberry Pi receives the computed timings and controls the traffic lights accordingly, incorporating a countdown timer for enhanced traffic management.

## System Workflow

1. **Video Capture:** Raspberry Pi captures short video feeds for each lane.
2. **Video Transmission:** The captured videos are transmitted to the server via FastAPI.
3. **Video Processing:** The server processes the videos using YOLOv5 to detect vehicles and determine the vehicle count in each lane.
4. **Traffic Timing Calculation:** Based on the vehicle count, the system calculates the optimal green and red light durations for the X and Y lanes.
5. **Traffic Light Control:** The Raspberry Pi controls the traffic lights using the calculated durations, with a real-time countdown display.

### Example Output
The system returns the following data structure, where `x1_vehicles`, `x2_vehicles`, `y1_vehicles`, and `y2_vehicles` represent vehicle counts in the respective lanes, and `x_green_time` and `y_green_time` represent the green light durations:

```json
{
  "id": "20240413060929emkax651ip2ff3e1acea50443b9b6ed854613634e6",
  "x1_vehicles": 0,
  "x2_vehicles": 0,
  "y1_vehicles": 0,
  "y2_vehicles": 0,
  "x_green_time": 60,
  "y_green_time": 60
}
```

## Project Structure

The project is organized as follows:

```
project
├── LICENSE
├── README.md
├── assets
│   └── output.gif
├── config  # Configuration files for the project
│   └── ... (other config-related files)
├── deep_sort  # Deep Sort tracking implementation
│   ├── configs  # Config files for Deep Sort
│   ├── deep  # Deep learning-related code
│   ├── sort  # Sorting algorithm implementation
│   ├── utils  # Utility scripts for Deep Sort
│   ├── deep_sort.py  # Main Deep Sort script
│   └── __init__.py  # Initialization script
├── module  # Custom modules for the project
│   └── __pycache__  # Compiled Python files
├── traffic  # Traffic light control logic
│   ├── controller.py  # Main controller for traffic light logic
│   ├── model.py  # Models for traffic data
│   ├── service.py  # Services for processing and logic
│   ├── __init__.py  # Initialization script
├── uploads  # Directory for video uploads from Raspberry Pi
│   └── ... (sample videos for testing)
├── yolov5  # YOLOv5 model integration
│   ├── classify  # YOLOv5 classification scripts
│   ├── data  # Data handling scripts for YOLOv5
│   ├── models  # YOLOv5 models
│   ├── segment  # Segmentation models and scripts
│   ├── utils  # Utility scripts for YOLOv5
│   ├── detect.py  # Object detection script using YOLOv5
│   ├── export.py  # Script for exporting models
│   ├── train.py  # Script for training YOLOv5 models
│   ├── hubconf.py  # Hub configuration for YOLOv5
│   ├── requirements.txt  # Python dependencies for YOLOv5
│   └── ... (other YOLOv5 related files)
└── yolov5s.pt  # YOLOv5 model weights file
```

## Setup Instructions

### 1. Clone the YOLOv5 Repository
```bash
git clone https://github.com/derekzyl/computer-vision-traffic-control.git
```

### 2. Install Required Dependencies
Install the necessary libraries for both the YOLOv5 and FastAPI components:
```bash
pip install -r requirements.txt && cd yolov5 && pip install -r requirements.txt
```

### 3. Run the FastAPI Server
Start the server using:
```bash
uvicorn main:app --reload
```

### 4. Deploy to Cloud Storage 
for faster image/video processing send to a server that is used for computer vision/ml

