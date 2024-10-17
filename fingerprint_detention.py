import os
import cv2

sample = cv2.imread("SOCOFing\\Altered\\Altered-Hard\\150__M_Right_index_finger_Obl.BMP")
#sample = cv2.imread("SOCOFing\\Altered\\Altered-Hard\\50__M_Left_index_finger_Obl.BMP")
#sample = cv2.imread("SOCOFing\\Altered\\Altered-Hard\\50__M_Left_middle_finger_Obl.BMP")
#sample = cv2.imread("SOCOFing\\Altered\\Altered-Hard\\50__M_Right_little_finger_Obl.BMP")

best_score = 0
filename = None
image = None
kp1, kp2, mp = None, None, None

counter = 0
for file in [file for file in os.listdir("SOCOFing\\Real")][:1000]:
    if counter%10 == 0:
        print(counter)
        print(file)

        counter += 1
    fingerprint_image = cv2.imread("SOCOFing\\Real\\"+ file)
    sift = cv2.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

    matches = cv2.FlannBasedMatcher({'algorithm':1, 'trees':10},{}).knnMatch(descriptors_1, descriptors_2, k=2)
    match_points = []

    for p, q in matches:
        if p.distance <0.1 * q.distance:
            match_points.append(p)

    keypoints = 0
    if len(keypoints_1) < len(keypoints_2):
        keypoints = len(keypoints_1)
    else:
        keypoints = len(keypoints_2)

    if len(match_points) / keypoints*100 > best_score:
        best_score = len(match_points)/keypoints*100
        filename = file
        image = fingerprint_image
        kp1, kp2, mp = keypoints_1, keypoints_2, match_points

print("BEST MATCH:" + file)
print("Score: " + str(best_score))

result = cv2.drawMatches(sample, kp1, image,kp2,mp,None)
result = cv2.resize(result, None, fx=4, fy=4)
cv2.imshow("results", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


