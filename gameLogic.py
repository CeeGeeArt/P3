import math
import cv2
import numpy as np
# import the rest of the files...
import Team
import Main
import Mirror
import Laser
import Blocker
import Detection
import Target

# Variables
targetCount = 0
totalPointCount = 0
maxPoints = 11
specialTarget = np.random.randint(1, 10)
targetArray = []

# Team name input.
name1 = input('Enter the blue teams name: ')
name2 = input('Enter the red teams name: ')

# Prepare video capture.
cap = cv2.VideoCapture(0)

# Loop which runs the game.
while (1):
    _, frame = cap.read()

    # Activate two team objects. They contain points and a name.
    team1 = Team.Team(name1)
    team2 = Team.Team(name2)

    # Detection. Should return a box.
    red_boxes = Detection.detectionRed(frame)
    blue_boxes = Detection.detectionBlue(frame)

    # Create mirrors and blockers from the detected boxes
    img = cv2.imread('test.jpg')
    mirrorBLockerList = []
    for i in range(len(red_boxes)):
        point1, point2, point3, point4 = red_boxes[i]
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3
        x4, y4 = point4
        tempBlocker = Blocker.Blocker(x1, y1, x2, y2, x3, y3, x4, y4, img)
        mirrorBLockerList.append(tempBlocker)
    for i in range(len(blue_boxes)):
        point1, point2, point3, point4 = blue_boxes[i]
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3
        x4, y4 = point4
        tempMirror = Mirror.Mirror(x1, y1, x2, y2, x3, y3, x4, y4, img)
        mirrorBLockerList.append(tempMirror)



    # Draws contours for testing purposes.
    for i in range(len(red_boxes)):
        cv2.drawContours(frame, [red_boxes[i]], 0, (0, 0, 255), 2)
    for i in range(len(blue_boxes)):
        cv2.drawContours(frame, [blue_boxes[i]], 0, (255, 0, 0), 2)

    # Laser. Should return an array/list of laser objects.
    # Each laser should contain two coordinates and a team.

    # Activate Collision. Should return an image to draw on the playspace and create new laser objects
    lasers, frame = Main.laserFire(frame, 20, 0.2, mirrorBLockerList, frame)
    for i in range(len(lasers)):
        lasers[i].drawLaser()
    cv2.imshow('lasers', frame)

    # Activate the target. Should return the team that scored as well as the amount of points scored.
    # Initialize a target when there's less than 2 and the game is still running.
    while targetCount < 2 and totalPointCount < maxPoints:
        totalPointCount += 1
        x = np.random.randint(0, 1000)
        y = np.random.randint(0, 1000)
        if totalPointCount is specialTarget:
            temp_target = Target.Target(True, 0, 0)
            targetArray.append(temp_target)
        else:
            temp_target = Target.Target(False, 0, 0)
            targetArray.append(temp_target)

    # # Call the targetCollision function.
    # for i in range(len(targetArray)):
    #     collision, doublePoints = targetArray[i].targetCollision(lasers)
    #     # should check if there is collision and what team has achieved it. Then checks how many points they scored.
    #     if collision:
    #         if team1:
    #             if doublePoints:
    #                 team1.addDoublePoints()
    #             else:
    #                 team1.addPoint()
    #         if team2:
    #             if doublePoints:
    #                 team2.addDoublePoints()
    #             else:
    #                 team2.addPoint()
    #     targetCount -= 1
    #     # Remove current targetArray index

    team1.addPoint()
    team1.addPoint()
    team2.addPoint()

    # Code for testing the Team class.
    # if team1.getPoints() < team2.getPoints():
    #     print(team2.getName() + " is in the lead with " + str(team2.getPoints()) + " points")
    # else:
    #     print(team1.getName() + " is in the lead with " + str(team1.getPoints()) + " points")

    # Wait until q is pressed to exit loop. This only works when openCV has an active window.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # break the loop after the first run for testing purposes.
    #break