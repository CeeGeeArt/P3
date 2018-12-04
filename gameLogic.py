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
frameCount = 0
targetCount = 0
totalPointCount = 0
maxPoints = 5
specialTarget = np.random.randint(1, 10)
targetArray = []

font = cv2.FONT_HERSHEY_SIMPLEX

testImg = cv2.imread('testSmall.jpg')

# Team name input.
name1 = input('Enter the green teams name: ')
name2 = input('Enter the purple teams name: ')

# Prepare video capture.
cap = cv2.VideoCapture(1)
_, frame = cap.read()


# Activate two team objects. They contain points and a name.
team1 = Team.Team(name1)
team2 = Team.Team(name2)

# Teamcolors
color1 = (60, 224, 31)
color2 = (244, 66, 203)

# Laser start position and direction
# Team 1
vRow, vCol, vCH = frame.shape
start_X1 = 200
start_Y1 = int(vRow/2)
end_X1 = 0
end_Y1 = int(vRow/2)
team1_laser_start = Laser.Laser(start_X1, start_Y1, end_X1, end_Y1)

# Team 2
start_X2 = vCol-200
start_Y2 = int(vRow/2)
end_X2 = vCol
end_Y2 = int(vRow/2)
team2_laser_start = Laser.Laser(start_X2, start_Y2, end_X2, end_Y2)

# Crop values
cropYTop = 90
cropYbottom = 95
cropXLeft = 112
cropXRight = 132

# Loop which runs the game.
while (1):
    _, frame = cap.read()
    croppedFrame = frame[cropYTop:-cropYbottom, cropXLeft:-cropXRight]
    frameCount += 1

    # runs the code every third frame to reduce load and make the laser slightly less jittery.
    if frameCount % 1 is 0:

        # Detection. Should return a box.
        red_boxes = Detection.detectionRed(frame)
        blue_boxes = Detection.detectionBlue(frame)

        # Create mirrors and blockers from the detected boxes
        img = cv2.imread('testSmall.jpg')
        mirrorBLockerList = []
        for i in range(len(red_boxes)):
            point1, point2, point3, point4 = red_boxes[i]
            x1, y1 = point1
            x2, y2 = point2
            x3, y3 = point3
            x4, y4 = point4
            tempBlocker = Blocker.Blocker(x1, y1, x2, y2, x3, y3, x4, y4, frame)
            mirrorBLockerList.append(tempBlocker)
        for i in range(len(blue_boxes)):
            point1, point2, point3, point4 = blue_boxes[i]
            x1, y1 = point1
            x2, y2 = point2
            x3, y3 = point3
            x4, y4 = point4
            tempMirror = Mirror.Mirror(x1, y1, x2, y2, x3, y3, x4, y4, frame)
            mirrorBLockerList.append(tempMirror)



        # # Draws contours for testing purposes.
        for i in range(len(red_boxes)):
            cv2.drawContours(img, [red_boxes[i]], 0, (0, 0, 255), 2)
        for i in range(len(blue_boxes)):
            cv2.drawContours(img, [blue_boxes[i]], 0, (255, 0, 0), 2)

        # Laser. Should return an array/list of laser objects.
        # Each laser should contain two coordinates and a team.

        # Activate Collision. Should return an laser to draw on the playspace and create new laser objects
        green_lasers, frame = Main.laserFire(team1_laser_start, 20, 0.2, mirrorBLockerList, frame)
        for i in range(len(green_lasers)):
            green_lasers[i].drawLaser(color1, img)

        purple_lasers, frame = Main.laserFire(team2_laser_start, 20, 0.2, mirrorBLockerList, frame)
        for i in range(len(purple_lasers)):
            purple_lasers[i].drawLaser(color2, img)

        # Activate the target. Should return the team that scored as well as the amount of points scored.
        # Initialize a target when there's less than 2 and the game is still running.
        while targetCount < 2 and totalPointCount < maxPoints:
            totalPointCount += 1
            targetCount += 1
            x = np.random.randint(cropXLeft, vCol-cropXRight)
            y = np.random.randint(cropYTop, vRow-cropYbottom)
            if totalPointCount is specialTarget:
                temp_target = Target.Target(True, x, y)
                targetArray.append(temp_target)
            else:
                temp_target = Target.Target(False, x, y)
                targetArray.append(temp_target)

        # Call the targetCollision function.
        for i in range(len(targetArray)):
            # print("New target collision check -----------------------------------------------------")
            green_collision, green_doublePoints = targetArray[i].targetCollision(green_lasers)
            purple_collision, purple_doublePoints = targetArray[i].targetCollision(purple_lasers)
            # should check if there is collision and what team has achieved it. Then checks how many points they scored.
            if green_collision:
                if green_doublePoints:
                    team1.addDoublePoints()
                else:
                    team1.addPoint()
            if purple_collision:
                if purple_doublePoints:
                    team2.addDoublePoints()
                else:
                    team2.addPoint()
            if green_collision or purple_collision:
                # Remove current targetArray index
                targetCount -= 1
                targetArray.pop(i)
                break

        # Code for testing the Team class.
        if team1.getPoints() < team2.getPoints() and totalPointCount == maxPoints:
            print(team2.getName() + " is in the lead with " + str(team2.getPoints()) + " points")
            cv2.putText(img, "Team: "+team2.getName()+" has won", (150, 240), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif team2.getPoints() < team1.getPoints() and totalPointCount == maxPoints:
            print(team1.getName() + " is in the lead with " + str(team1.getPoints()) + " points")
            cv2.putText(img, "Team: "+team1.getName()+" has won", (150, 240), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

        print(team2.getName() + " has scored " + str(team2.getPoints()) + " points")
        print(team1.getName() + " has scored " + str(team1.getPoints()) + " points.")

        # Draw the objects
        for i in range(len(targetArray)):
            targetArray[i].drawCircle(img)

        croppedImg = img[cropYTop:-cropYbottom, cropXLeft:-cropXRight]
        cv2.namedWindow("testIMG", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("testIMG", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('testIMG', croppedImg)
        cv2.imshow('test', croppedFrame)
        cv2.imshow('lasers', frame)

        # Wait until q is pressed to exit loop. This only works when openCV has an active window.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        # break the loop after the first run for testing purposes.
        #break