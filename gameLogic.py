import math
import cv2
import numpy as np
# import the rest of the files...
import Team
import Detection
import Target

# Variables

# Team names should be something that can be input by the user
name1 = input('Enter the blue teams name: ')
name2 = input('Enter the red teams name: ')

# Prepare video capture
cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()

    # Activate two team objects. They contain points and a name.
    team1 = Team.Team(name1)
    team2 = Team.Team(name2)

    # Detection. Should return a box.
    red_boxes = Detection.detectionRed(frame)
    blue_boxes = Detection.detectionBlue(frame)

    for i in range(len(red_boxes)):
        cv2.drawContours(frame, [red_boxes[i]], 0, (0, 0, 255), 2)

    for i in range(len(blue_boxes)):
        cv2.drawContours(frame, [blue_boxes[i]], 0, (255, 0, 0), 2)

    cv2.imshow('boxFrames', frame)

    # Laser. Should return an array/list of laser objects.
    # Each laser should contain two coordinates and a team.

    # Activate Collision. Should return an image to draw on the playspace and create new laser objects

    # Activate the target. Should return the team that scored as well as the amount of points scored.
    # Lines to test the Target class
    line1 = [(100, 100), (-100, -100)]
    line2 = [(100, 100), (100, 200)]
    test_array = np.array([line2])

    # Initialize a target and call the targetCollision function.
    new_target = Target.Target(False, 0, 0)
    collision, doublePoints = new_target.targetCollision(test_array)
    print("A line collided: " + str(collision))


    team1.addPoint()
    team1.addPoint()
    team2.addPoint()

    # Code for testing the Team class.
    if team1.getPoints() < team2.getPoints():
        print(team2.getName() + " is in the lead with " + str(team2.getPoints()) + " points")
    else:
        print(team1.getName() + " is in the lead with " + str(team1.getPoints()) + " points")

    # Wait until q is pressed to exit loop. This only works when openCV has an active window.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # break the loop after the first run for testing purposes.
    #break