
<div align="center">

# Traffic Control System using FastAPI and YOLOv5

</div>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

<div align="center">

<img src="assets/output.gif" width="1000px" height="600px">

</div>

### Introduction

This project utilizes FastAPI and YOLOv5 to develop a traffic control system that processes four short videos and returns traffic control parameters for both X lane and Y lane.

The system returns the following data:

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

Where:

- `x1_vehicles`, `x2_vehicles`, `y1_vehicles`, `y2_vehicles` represent the vehicle count in X and Y lanes respectively.
- `x_green_time` and `y_green_time` represent the green light duration for X and Y lanes respectively.

### Pre-requisites

1. Clone the legacy YOLOv5 Repository

```bash
git clone https://github.com/ultralytics/yolov5.git
```

2. Install the required libraries

```bash
pip install -r requirements.txt && cd yolov5  && pip install -r requirements.txt
```

### Directory Structure

After completing the above steps, your directory structure should resemble the following:

project
├── LICENSE
├── README.md
├── assets
│   └── output.gif
├── deep_sort  # Folder containing Deep Sort tracking code
│   └── ... ( contains other Deep Sort related files)
├── inference  # Folder potentially related to model inference
│   └── ... ( contains other inference related files)
├── runs  # Folder potentially related to model training runs
│   └── ... ( contains other run related files)
├── templates  # Folder potentially related to template files
│   └── ... ( contains other template related files)
├── uploads
│   └── ...sample videos for testing ( contains other uploaded files)
├── yolov5  # Folder containing YOLOv5 object detection code
│   ├── .env  # Likely an environment variable file
│   ├── light.py  # Script potentially related to light control
│   ├── main.py  # Main script for the project
│   ├── Pipfile  # Likely a lockfile for Pip package manager
│   ├── raspberry_code.py  # Script potentially related to Raspberry Pi code
│   ├── requirements.txt  # File containing required Python libraries
│   ├── test.py  # Script for testing purposes
│   ├── tracker.py  # Script for running the vehicle counting algorithm
│   ├── traffic_time.py  # Script potentially related to traffic light timing
│   ├── videos.py  # Script potentially related to video processing
│   ├── x.jpg  # Image file
│   └── x.txt  # Text file
└── yolov5s.pt  # YOLOv5 model weights file

### Usage

Run the server using the following command:

```bash
uvicorn main:app --reload

```

 you can upload to a cloud storage immediately

</div>
