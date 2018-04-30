import numpy as np
import cv2

dev_id = 1
cap = cv2.VideoCapture(dev_id)
#dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
#dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)

# Camera matrix and dsistortion parameters
A = np.matrix([[538.9863478438378, 0, 328.326117302372], [0, 539.0749475096734, 209.4122266512357], [0, 0, 1]])
dist_coeff = np.r_[0.06843722986120428, -0.1229275646593768, -0.01015740867557202, 0.00886817786361772, 0]
marker_length = 0.0265

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners, ids, rejected = cv2.aruco.detectMarkers(image=gray,dictionary=dictionary, cameraMatrix=A, distCoeff=dist_coeff)

    #print(corners,ids,len(rejected))
    
    marker_1001_found = False
    if len(corners) > 0:
        cv2.aruco.drawDetectedMarkers(gray, corners, ids)
        rvec, tvec, obj_pts = cv2.aruco.estimatePoseSingleMarkers(corners, marker_length, A, dist_coeff)
        for i in [0,len(ids)-1]:
            print(i)
            if ids[i] == 1001:
                marker_1001_found = True
                print('Marker 1001 is at position:', rvec[i], tvec[i])
    if not marker_1001_found:
        print('Marker 1001 not found')

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q')
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
