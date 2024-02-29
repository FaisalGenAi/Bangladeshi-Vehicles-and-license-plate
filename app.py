#----------------- FPS Code ------------------------

# from ultralytics import YOLO
# import cv2
# import time


# # load models
# coco_model = YOLO('yolov8n.pt')
# license_plate_detector = YOLO('best.pt')


# # Capture video from webcam
# # cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("2.mp4")
# ret = True

# while ret:
#     # Capture frame-by-frame
#     ret, frame = cap.read()

    # fps = cap.get(cv2.CAP_PROP_FPS)
    # fps = str(fps)


    # cv2.putText(frame, fps, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     cv2.imshow("Frame", frame)
#     # Exit if 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()





#-------------------------###### fps Code Start #########-----------------------------#

# from ultralytics import YOLO
# import cv2
# import time

# # Capture video from webcam
# cap = cv2.VideoCapture(0)


# # Initialize previous and current frame time
# prev_frame_time = 0
# curr_frame_time = 0

# # Initialize fps
# fps = 0

# while True:
#     # Update previous frame time
#     prev_frame_time = curr_frame_time
#     # Update current frame time
#     curr_frame_time = time.time()
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Calculate fps
#     fps = 1 / (curr_frame_time - prev_frame_time)
#     # Convert fps to integer and string
#     fps = int(fps)
#     fps = str(fps)
#     # Display fps on the frame
#     cv2.putText(frame, fps, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#     # Show the frame
#     cv2.imshow("Frame", frame)
#     # Exit if 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()

#-------------------------###### fps Code End #########-----------------------------#



from ultralytics import YOLO
import cv2
from sort.sort import *
import time

mot_tracker = Sort()


# load models
model = YOLO('yolov8n.pt')
model1 = YOLO('best1.pt')


# Capture video from webcam
# cap = cv2.VideoCapture(0)
vehicles = [ 2, 3, 5, 7]
cap = cv2.VideoCapture("4.mp4")
ret = True

while ret:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # fps = cap.get(cv2.CAP_PROP_FPS)
        # fps = str(fps)
        # cv2.putText(frame, fps, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


        #vehicle tracking
        plate = []   
        cars = []
        result = model(frame)[0]
        for car in result.boxes.data.tolist():
            x1, y1, x2, y2, scores, class_id = car
            # x = int(x1)
            # y = int(y1)
            # w = int(x2)
            # h = int(y2)
            x = x1
            y = y1
            w = x2
            h = y2
            class_id = int(class_id)
            if class_id in vehicles:
               cars.append([x, y, w, h])
               print(class_id)

        track_ids = mot_tracker.update(np.asarray(cars)) 
        # frame = cv2.resize(frame, (320, 240))
        

        license_plates = model1(frame)[0]
        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate
            plate.append([x1, y1, x2, y2])

        # print(track_ids)
        # for (x, y, w, h) in cars:
        for (x, y, w, h) in plate:
            x = int(x)
            y = int(y)
            w = int(w)
            h = int(h)
            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


        cv2.imshow("Frame", frame)
        # Exit if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()