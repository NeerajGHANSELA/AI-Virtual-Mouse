# AI-Virtual-Mouse

AI-powered hand tracking system that controls your mouse cursor through webcam gestures - no physical contact needed

A computer vision-based touchless mouse control system that lets you navigate your computer using hand gestures captured through your webcam.

## Overview

VirtualMouse uses MediaPipe's hand tracking model and OpenCV to detect hand landmarks in real-time, translating natural hand movements into precise cursor control. Simply raise your index finger to move the mouse, and pinch your fingers together to click—no physical mouse required.

**Key Features:**

- 🎯 Real-time hand tracking and gesture recognition
- 🖱️ Smooth cursor control with anti-jitter algorithms
- 👆 Intuitive gestures: index finger for navigation, index + middle finger pinch to click
- ⚡ Optimized for performance with frame reduction techniques
- 🎥 Works with any standard webcam

**Technologies:** Python • MediaPipe • OpenCV • NumPy • AutoPy

## Installation

### Prerequisites

- Python 3.7 or higher
- Webcam

### Setup

1. Clone the repository:

```bash
git clone https://github.com/NeerajGHANSELA/AI-Virtual-Mouse.git
cd AI-Virtual-Mouse
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python virtualMouse.py
```

## Usage

Once the application starts, your webcam will activate and you can control your mouse using these gestures:

| Gesture                                               | Action                |
| ----------------------------------------------------- | --------------------- |
| ☝️ **Index finger up** (middle finger down)           | Move the mouse cursor |
| ✌️ **Index + Middle fingers up, then pinch together** | Click                 |

**Tips for best performance:**

- Ensure good lighting for optimal hand detection
- Keep your hand within the purple boundary box displayed on screen
- Small hand movements translate to full screen cursor movement (no need to stretch!)
