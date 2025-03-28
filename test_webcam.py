import cv2

def test_webcam(device=0):
    #Variable Cap that is acessing webcam. If initially doesn't work try changing device number
    cap = cv2.VideoCapture(device)
    #Check if correct device was used and webcam was opened
    if not cap.isOpened():
        print("Error: Could not open webcam (device {device}). Try changing the device number.")
        return
    #while loop to keep the webcam open
    while cap.isOpened():
        #Read Feed from webcam
        ret, frame = cap.read()
        #Show to screen
        cv2.imshow('OpenCV Feed', frame)

        #if the user presses the q key, the webcam will close       
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    #Change to 1, 2, etc if the default device doesn't work
    test_webcam(device=0)











