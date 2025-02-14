Object Tracking using OpenCV 

Introduction 
In this project, I developed an object tracking system using OpenCV. The main idea is to detect and track an object based on its color (currently white). The program processes live video from the camera, identifies the object, and draws a bounding box around it as it moves. Additionally, I added a feature to capture a screenshot when pressing a specific key.  

How does the program work? 
1. Camera Activation: When the program starts, it opens the camera and begins capturing video.  
2. Color-Based Object Detection: The program converts the frame to the HSV color space and applies a filter to detect objects with a specific color range (white in this case).  
3. Contour Detection: The program finds the object's shape and determines its position.  
4. Tracking and Bounding Box: If an object is detected, a green rectangle is drawn around it to highlight the tracking.  
5. Saving a Screenshot: Pressing *s* saves a screenshot of the current frame with the tracked object.  
6. Exiting the Program: Pressing *q* stops the camera and closes all windows.  

How do I run the program? 
1. First, I ensured that the required libraries were installed:  
   bash
   pip install opencv-python numpy
   
2. Then, I ran the script using Python.  
3. The camera opened, and the program started tracking the white object in real time.  
4. Pressing *s* saved a screenshot.  
5. Pressing *q* exited the program.  

Notes 
- The program currently tracks white objects, but I can modify the lower_white and upper_white values to track other colors.  
- This project combines color recognition and object tracking, meaning it only tracks objects of a specific color rather than detecting all objects.  
- I can adjust the minimum contour area in cv2.contourArea(contour) > 1000 to change the sensitivity of object detection.  
