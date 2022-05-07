import mediapipe as mp
import cv2
v_cap=cv2.VedioCapture(0)
hands=mp.solutions.hands
m_hand=hands.hands(min_detection_confidence=0.8,min_tracking_confidence=0.9)
m_drawing=mp.solutions.drawing_utils
"""The input collected form the mouse.py is used by the landmark function for runnig the source pipe"""
def hand_landmarks(img):
    landmark_list=[0,0,0]
    "The basic postions of each input form the media pipe are stored as the list objects with (h,w,c) where c is the channel"
    landmark_positions=m_hand.process(img)
    "Extracting the positions of the image scanned"
    l_check=l_positions.multi_hand_landmarks
    "if multiple positions where fing are tracked then the signal like t or f along with co-ordinates are saved in the l_check"
    if l_check:
        for h in l_check:
            for i,l_marks in enumerate(h.landmark):
                draw.draw_handmarks(img,h,hands.HAND_CONNECTIONS)
                h,w,c=img.shape
                center_x,center_y=int(landmarks.x * w),int(landmarks.y * w)
                landmark_list.append([i,center_x,center_y])
    return landmark_list
def fingertips(landmarks):
    fingertips_res=[]
    tipids=[4,8,12,16,20]
    """This are the tip values of the every finger when thevirtual ploting is done"""
    "For checking whetehr the thub is closed or open we need to compare the tip value of the thumb finger with the mid value of the thumb finger"
    "So if the thumb finger tip value which is 4 when it is opened, if it is closed then the thumb tip value becomes 0, is comapred against the mid value of te thumb finger"
    if landmarks[tipids[0]][1]]>landmarks[tipids[0]-1]][1]:
        fingertips_res.append(1)
    else:
        fingertips.apppend(0)
    "So, once we get whether the thumb is opened or closed we can get a sign that can be used as shortcutsign to do..."
    "Same goes with the res fingers to"
    for i in range(1,5):
        if landmarks[tipids[i]][2]]<landmarks[tipids[i]-3]][2]:
            fingertips_res.append(1)
        else:
            fingertips_res.append(0)
    return fingertips_res

while True:
    check,img=v_cap.read()
    image_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    lmlist=hand_landmarks(image_rgb)
    if len(lmlist)!=0:
        fingers=fingertips(lmlist)
        print(fingers)
    cv2.imshow("Wbcame Turned On",img)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
v_capture.release()
cv2.destroyAllWindows()
