import numpy as np
import cv2

dev_id = 1
cap = cv2.VideoCapture(dev_id)
#dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
#dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)

# Camera matrix and dsistortion parameters
A = np.matrix([[208, 0, 320], [0, 300, 240], [0, 0, 1]])
dist_coeff = np.r_[0.0968, -0.0713, 0.00218, -0.0111, 0]
marker_length = 0.18

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners, ids, rejected = cv2.aruco.detectMarkers(image=gray,dictionary=dictionary, cameraMatrix=A, distCoeff=dist_coeff)

    #print(corners,ids,len(rejected))
    
    marker_found = False
    if len(corners) > 0:
        cv2.aruco.drawDetectedMarkers(gray, corners, ids)
        rvec, tvec, obj_pts = cv2.aruco.estimatePoseSingleMarkers(corners, marker_length, A, dist_coeff)
        for i in [0,len(ids)-1]:
            print(i)
            if ids[i] == 0:
                marker_found = True
                print('Marker is at position:', rvec[i], tvec[i])
    if not marker_found:
        print('Marker not found')

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
