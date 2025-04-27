# Blink-to-Scroll-
This project allows you to control your computer's scrolling functionality using eye blinks. It uses OpenCV and MediaPipe for real-time face and eye landmark detection, and pyautogui to simulate scrolling based on eye blinks.

Features:
Eye Blink Detection: Detects blinks using the distance between the top and bottom landmarks of the left eye.

Scroll Control: When a blink is detected, the system simulates a scroll down action using pyautogui.

Real-time Face Mesh: Utilizes MediaPipe for face and eye landmark tracking.

Requirements:
To run the project, you need the following Python packages:

opencv-python (for webcam capture and image processing)

mediapipe (for face and eye landmark detection)

pyautogui (for simulating the scroll action)

You can install the required libraries using pip:


pip install opencv-python mediapipe pyautogui
How It Works:
Blink Detection: The system detects the eyes' top and bottom landmarks. It calculates the Eye Aspect Ratio (EAR) to detect if the eyes are closed.

Scroll Action: When the system detects a blink (eyes closed for a certain amount of time), it triggers a scroll action using pyautogui.

Cooldown: To prevent multiple triggers from a single blink, there is a cooldown period (default: 1.2 seconds).

How to Use:
Clone the repository to your local machine.

Run the Python script:

python eye_blink_scroll.py
The webcam window will open. Blink your eyes to trigger the scrolling action.

Press 'q' to quit the application.

Notes:
The system detects blinks based on the vertical distance between the top and bottom of the left eye. 
You can adjust the sensitivity by modifying the EAR_THRESHOLD.

You can change the scrolling behavior by modifying the pyautogui.scroll() method's argument (e.g., increase or decrease the scroll amount).

This script requires a webcam to detect your face and eyes.

License
This project is open source and available under the MIT License.
