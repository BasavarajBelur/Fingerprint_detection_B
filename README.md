# Fingerprint_detection_B
Fingerprint recognition using Python, including pattern-oriented matching, correlation-oriented matching

# How it works
Fingerprint scanners work by capturing the pattern of ridges and valleys on a finger. There are two separate stages involved in using a system. First, you have to go through a process called enrollment, where the system learns about all the people it will have to recognize. As a finger rests on the touch-capacitive surface, the device measures the charge; ridges exhibit a change in capacitance, while valleys produce practically no change at all. The sensor uses all this data to accurately map out prints. During enrollment, each person’s fingerprints are scanned, analyzed, and then stored in a coded form on a secure database. Typically it takes less than a half-second to store a person’s prints.

# How fingerprint stored and compared
A computer can compare fingerprints by identifying key features- a bit like drawing lines between them and then measuring the distances and angles between them. Algorithms can turn patterns like this into unique numeric codes. Comparing fingerprints is then simply a matter of comparing unique codes. If the codes match, the prints match, and the person gains access.

# Fingerprint Recognition OpenCV Python
This resource provides a Python library for fingerprint recognition and includes dataset connection code

# CNN-Model-Detecting-Liveness-of-Fingerprint-using-Deep-Learnig
This resource uses a convolutional neural network (CNN) and deep learning to detect the liveness of a fingerprint.

# Dataset link#
https://www.kaggle.com/datasets/ruizgara/socofing


![image](https://github.com/user-attachments/assets/5e4b33b2-5d3a-4601-ae4a-47082a0cdd07)


# Steps Involved in Fingerprint Recognition using Python Project
Step 1 – Get the input image and preprocess the collected image.

Step 2 – Segment the image block which has a central position of the fingerprint.

Step 3 – Implement fuzzy rule logics over feature points of the fingerprint.

**Note:**- datasets files/folders should be in the same directory where finger_detection file is running 
