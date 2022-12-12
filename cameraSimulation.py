import cv2 

vid = cv2.VideoCapture('./in.avi')

while True:
    isTrue, frame = vid.read()  
    
    cv2.imshow("Original Source",frame) 
    if cv2.waitKey(20) & 0xff==ord('d'):
        break

vid.release()
cv2.destroyAllWindows()

