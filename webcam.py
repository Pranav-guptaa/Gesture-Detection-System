import numpy as np
import cv2
from fastai.vision import *

defaults.device = torch.device('cpu')

path = 'D:\\DATA\\(SEMESTER-4)\\Minor Project\\final-asl'
imgpath = 'D:\\DATA\\(SEMESTER-4)\\Minor Project\\final-asl\\pred-image.jpg'

cap = cv2.VideoCapture(0)
cap.set(3, 640) # width, height
cap.set(4, 480)

font = cv2.FONT_HERSHEY_SIMPLEX

learn = load_learner(path)

def predict():
    img = open_image(imgpath)
    
    pred_class, pred_idx, outputs = learn.predict(img)
    return pred_class


def webcam_stream():

    fps = 0

    prediction = ''
    title = 'ASL Recoginition'
    help_text = 'Press R to Reset or Q to quit'

    while True:
        ret, frame = cap.read()

        if fps == 100:
            image = frame[50:300, 50:300]
            cv2.imwrite('pred-image.jpg', image)
            pred = predict()
            temp = str(pred)
            if temp == "space":
                prediction += " "
            elif temp == "del":
                prediction = prediction[:-1]
            elif temp == "nothing":
                prediction += ""
            else:
                prediction += temp
            fps = 0

        fps += 1

        cv2.putText(frame, title, (180, 30), font,
                    1, (0, 0, 0), 2, cv2.LINE_AA) 

        cv2.putText(frame, prediction, (50, 400), font,
                    2, (255, 255, 255), 2, cv2.LINE_AA) 
        #anti-aliased line

        cv2.putText(frame, help_text, (60, 450), font,
                    1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.rectangle(frame, (50, 50), (300, 300), (250, 0, 0), 2)
        cv2.imshow("ASL Prediction", frame)

        key = cv2.waitKey(1)
        if key == ord('r'):
            prediction = ""
        elif key == ord('q'):
            break


if __name__ == '__main__':
    webcam_stream()

cap.release()
cv2.destroyWindow("ASL Prediction")
