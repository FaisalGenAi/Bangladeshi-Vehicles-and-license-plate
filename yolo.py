# from ultralytics import YOLO

# # Load a model
# # model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model
# model = YOLO('best301.pt')

# # Run batched inference on a list of images
# # results = model("3.mp4")  # return a list of Results objects

# # # Process results list
# # for result in results:
# #     boxes = result.boxes  # Boxes object for bounding box outputs
# #     masks = result.masks  # Masks object for segmentation masks outputs
# #     keypoints = result.keypoints  # Keypoints object for pose outputs
# #     probs = result.probs  # Probs object for classification outputs
# #     result.show()  # display to screen  



# import cv2
# from ultralytics import YOLO

# # Load the YOLOv8 model

# # Open the video file
# video_path = "1.mp4"
# cap = cv2.VideoCapture(video_path)
# ret = True
# # Loop through the video frames
# while ret:
#     # Read a frame from the video
#     ret, frame = cap.read()

#     if ret:
#         # Run YOLOv8 inference on the frame
#         results = model(frame)

#         # Visualize the results on the frame
#         annotated_frame = results[0].plot()

#         # Display the annotated frame
#         cv2.imshow("YOLOv8 Inference", annotated_frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         # Break the loop if the end of the video is reached
#         break

# # Release the video capture object and close the display window
# cap.release()
# cv2.destroyAllWindows()


# import the opencv library 
import cv2 


# define a video capture object 
vid = cv2.VideoCapture(0) 

while(True): 
	
	# Capture the video frame 
	# by frame 
	ret, frame = vid.read() 
	# Display the resulting frame 
	cv2.imshow('frame', frame) 
	
	# the 'q' button is set as the 
	# quitting button you may use any 
	# desired button of your choice 
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
