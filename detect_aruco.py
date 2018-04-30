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

print(A)
print(dist_coeff)

ids = (1001)
obj_pts = (1)

board = cv2.aruco.GridBoard_create(markersX=1, markersY=1, markerLength=0.02, markerSeparation=0.01, dictionary=dictionary, firstMarker=1001)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    res = cv2.aruco.detectMarkers(image=gray,dictionary=dictionary, cameraMatrix=A, distCoeff=dist_coeff)
    print(res[0],res[1],len(res[2]))
    
    if len(res[0]) > 0:
        cv2.aruco.drawDetectedMarkers(gray,res[0],res[1])
        ret = cv2.aruco.estimatePoseSingleMarkers(res[0], 0.0265, A, dist_coeff)
        print(ret[0][0],ret[1][0])
    
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
