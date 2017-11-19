# import the necessary packages
from collections import deque
import numpy
import argparse
import imutils
import cv2
from ball import Ball
from vector import Vector
from hippo import Hippo

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
                help="max buffer size")
args = vars(ap.parse_args())
# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
redLower = (0, 136, 162)
redUpper = (255, 255, 255)
pts = deque(maxlen=args["buffer"])
arrBalls = []
hippos = []
fps = 40
first = True

# 0 - orange , 1 = green, 2 = yellow
for i in range(0, 3):
    temp = Hippo(i)
    hippos.append(temp)

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
    camera = cv2.VideoCapture(0)

# otherwise, grab a reference to the video file
else:
    camera = cv2.VideoCapture(args["video"])
# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if args.get("video") and not grabbed:
        break

    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=600)
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # construct a mask for the color "red", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, redLower, redUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    # only proceed if at least one contour was found
    for i in range(0, len(cnts)):
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        center = None
        ((x, y), radius) = cv2.minEnclosingCircle(cnts[i])
        # M = cv2.moments(cnts[i])
        # center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if first:
            temp = Ball(Vector(x, y), radius, fps, 600)
            arrBalls.append(temp)
        else:
            # Make it more sophisticated
            for j in range(0, len(arrBalls)):
                a = numpy.array(arrBalls[j].pos.x, arrBalls[j].pos.y)
                b = numpy.array(x, y)
                if numpy.linalg.norm(a-b) <= 2*arrBalls[j].radius:
                    arrBalls[j].update(Vector(x, y))

                    if not hippos[0].move:
                        hippos[0].chomp(arrBalls[j].bool)

        # HOW TO SEND THIS DATA ? LINE 124

        first = False

        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)
            # cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # update the points queue
            # pts.appendleft(center)
            # loop over the set of tracked points
            # for i in xrange(1, len(pts)):
            # if either of the tracked points are None, ignore
            # them
            # if pts[i - 1] is None or pts[i] is None:
            #   continue

            # otherwise, compute the thickness of the line and
            # draw the connecting lines
            # thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
            # cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    # show the frame to our screen
    cv2.imshow("Frame", frame)

    for i in range(0, len(arrBalls)):
        if not arrBalls[i].endCheck:
            n = arrBalls[i].lastCheck
            arrBalls.pop(i)
            if not n == 3:
                hippos[n].counter()

    for i in range(0, 3):
        # SEND HIPPO DATA
        hippos[i].update


# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
