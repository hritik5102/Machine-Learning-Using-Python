from mtcnn.mtcnn import MTCNN
import cv2
img = cv2.imread("2.jpg")
detector = MTCNN()
print(detector.detect_faces(img))
#[{'box': [277, 90, 48, 63], 'keypoints': {'nose': (303, 131), 'mouth_right': (313, 141), 'right_eye': (314, 114), 'left_eye': (291, 117), 'mouth_left': (296, 143)}, 'confidence': 0.99851983785629272}]