import cv2

def camCapture(imgfilename):
    cap = cv2.VideoCapture(0)
    
    ret, frame = cap.read()
    
    cv2.imwrite("%s"%imgfilename, frame)
    
    cap.release()
    
    
if __name__ == "__main__":
    camCapture('testimage')