import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_white = np.array([0, 0, 200])   
upper_white = np.array([180, 50, 255])  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  
    mask = cv2.inRange(hsv, lower_white, upper_white)  

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("White Object Tracking", frame)

    key = cv2.waitKey(1) & 0xFF  
    if key == ord('s'):  
        cv2.imwrite("tracked_object.jpg", frame)  
        print("!image saved")

    elif key == ord("q"):  
        break

cap.release()
cv2.destroyAllWindows()