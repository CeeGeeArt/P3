import Mirror
import Collision
import Laser
import Blocker
import math
import cv2
#import Queue


img = cv2.imread('test.jpg')
height, width, channels = img.shape

def laserFire(videoFeed, totLaserPos, timePerPos):
    vRow, vCol, vCH = videoFeed.shape
    lsX = 500
    lsY = 0
    leX = 0
    leY = vRow

    # ------ Mirrors and blockers must have their points input in a counter clockwise manner. -----

    testBlock = Mirror.Mirror(299, 100, 299, 290, 200, 290, 200, 100, img)

    #testBlocker = Mirror.Mirror(500, 125, 550, 900, 700, 900, 700, 125, img)
    testBlocker = Mirror.Mirror(700, 125, 700, 900, 550, 900, 500, 125, img)

    testBlock1 = Mirror.Mirror(190, 350, 199, 900, 180, 900, 180, 350, img)

    testBlock2 = Mirror.Mirror(151, 450, 150, 950, 130, 950, 130, 450, img)

    #testBlock3 = Mirror.Mirror(240, 500, 242, 950, 400, 950, 500, 500, img)
    testBlock3 = Mirror.Mirror(500, 500, 400, 950, 242, 950, 240, 699, img)

    #testBlocker2 = Mirror.Mirror(100, height-50, 100, height, 900, height, 900, height-150, img)
    testBlocker2 = Mirror.Mirror(900, height - 170, 900, height, 100, height, 100, height - 50, img)

    #testBlocker3 = Mirror.Mirror(720, 90, 680, 300, 625, 300, 600, 50, img)
    #testBlocker4 = Mirror.Mirror(900, 50, 860, 300, 800, 300, 800, 50, img)
    #testBlocker2 = Blocker.Blocker(-5, -5, -5, height+5, width+5, height+5, width+5, -5, img)

    mirrorBLockerList = [testBlock, testBlocker, testBlock1, testBlock2, testBlock3, testBlocker2]
    finalLaser = None
    finalPointList = [(lsX, lsY)]
    prevReflect = None
    newReflect = None
    x3 = None
    y3 = None
    counter = 0

    current_laser = Laser.Laser(lsX, lsY, leX, leY, img)
    print("start while loop --------------------------------------------")
    while True:
        currentReflect = []
        prevReflect = newReflect
        colBool = []
        tempLaser = None
        reflectArray = []
        reflectArray2 = []

        print("start for loops")
        for i in range(len(mirrorBLockerList)):
            colBool.append(True)

        compareLaser = current_laser
        print("Compare laser:")
        print(compareLaser.getX1(), compareLaser.getY1(), compareLaser.getX2(), compareLaser.getY2())
        for j in range(len(mirrorBLockerList)):
            col = Collision.Collision(mirrorBLockerList[j], compareLaser)
            tempLaser = col.collisionDetection(img)
            colBool[j] = col.reflected

            if colBool[j] is True and j is not prevReflect:
                x = tempLaser.getX1()
                y = tempLaser.getY1()
                point = (x, y)
                reflectArray.append(point)
                end_x = tempLaser.getX2()
                end_y = tempLaser.getY2()
                end_point = (end_x, end_y)
                reflectArray2.append(end_point)
                print("current laser: " + str(tempLaser.getX1()) + " " + str(tempLaser.getY1()) + " " + str(
                    tempLaser.getX2())+ " " + str(tempLaser.getY2()))

                # Calculate the final laserPoint
                # x2 = tempLaser.getX2()
                # y2 = tempLaser.getY2()
                # lenAB = math.sqrt(pow(x - x2, 2.0) + pow(y - y2, 2.0))
                # x3 = int(x2 + (x2 - x) / lenAB * 10000)
                # y3 = int(y2 + (y2 - y) / lenAB * 10000)

                #current_laser = tempLaser
                currentReflect.append(j)

            # if counter > 4:
            #     if j is 2:
            #         print(tempLaser.getX1(), tempLaser.getY1())
            #         print(colBool[j])
            #     print("in loop info")
            #     print(prevReflect)
            #     print(currentReflect)
            #     print(reflectArray)
            #     print("in loop stop")

            #print("j = " + str(j))
            #print(colBool[j])

        print("reflectArray: " + str(reflectArray))

        # Remove point from the reflectArray that are placed in the wrong direction.
        real_direction_x = current_laser.getX2() - current_laser.getX1()
        real_direction_y = current_laser.getY2() - current_laser.getY1()
        print(real_direction_x, real_direction_y)
        compare_x = []
        compare_y = []
        popArray = []
        for i in range(len(reflectArray)):
            compare_x.append(reflectArray[i][0])
            compare_y.append(reflectArray[i][1])
            new_direction_x = compare_x[i] - current_laser.getX1()
            new_direction_y = compare_y[i] - current_laser.getY1()

            # Marks an entry for removal if the direction does not match with the known direction.
            # Checks x-axis
            if real_direction_x < 0:
                # Check
                if not (new_direction_x < 0):
                    popArray.append(i)
                    continue
            elif real_direction_x > 0:
                # check
                if not (new_direction_x > 0):
                    popArray.append(i)
                    continue
            else:
                # Direction = 0
                if not (new_direction_x is 0):
                    popArray.append(i)
                    continue

            # Checks y-axis
            if real_direction_y < 0:
                # Check
                if not (new_direction_y < 0):
                    popArray.append(i)
            elif real_direction_y > 0:
                # check
                if not (new_direction_y > 0):
                    popArray.append(i)
            else:
                # Direction = 0
                if not (new_direction_y is 0):
                    popArray.append(i)

        # Pops entries based on the markings. Reverse sorted to prevent interference with later iterations.
        print(popArray)
        popArray.sort(reverse=True)
        print(reflectArray)
        for i in range(len(popArray)):
            reflectArray.pop(popArray[i])
            reflectArray2.pop(popArray[i])
            currentReflect.pop(popArray[i])
        print(reflectArray)
        print("start point: " + str(finalPointList[len(finalPointList)-1]))

        breaking = False


        # Check which laser is the shortest
        print("start compare loop")
        startX, startY = finalPointList[len(finalPointList) - 1]
        compare = None
        ekstra_compare = None
        if len(reflectArray) > 1:
            print("BBC")
            for i in range(len(reflectArray)-1):
                x, y = reflectArray[i]
                x2, y2 = reflectArray[i+1]
                if i is 0:
                    # Find the closest of the first two points in the array.
                    distanceToPoint1 = math.sqrt(((startX - x) ** 2) + ((startY - y) ** 2))
                    distanceToPoint2 = math.sqrt(((startX - x2) ** 2) + ((startY - y2) ** 2))
                    if distanceToPoint1 < distanceToPoint2:
                        compare = reflectArray[i]
                        ekstra_compare = reflectArray2[i]
                        newReflect = currentReflect[i]
                    else:
                        compare = reflectArray[i+1]
                        ekstra_compare = reflectArray2[i+1]
                        newReflect = currentReflect[i+1]
                else:
                    # Compare the previously closest point to the next entry in the array.
                    x, y = compare
                    distanceToPoint1 = math.sqrt(((startX - x) ** 2) + ((startY - y) ** 2))
                    distanceToPoint2 = math.sqrt(((startX - x2) ** 2) + ((startY - y2) ** 2))
                    if distanceToPoint1 > distanceToPoint2:
                        compare = reflectArray[i + 1]
                        ekstra_compare = reflectArray2[i + 1]
                        newReflect = currentReflect[i + 1]
            finalPointList.append(compare)
            x, y = compare
            x2, y2 = ekstra_compare
            current_laser = Laser.Laser(x, y, x2, y2, img)

        elif len(reflectArray) > 0:
            print("BBB")
            finalPointList.append(reflectArray[0])
            newReflect = currentReflect[0]
            x, y = reflectArray[0]
            x2, y2 = reflectArray2[0]
            current_laser = Laser.Laser(x, y, x2, y2, img)

        else:
            print("No reflections")
            breaking = True
            x = current_laser.getX1()
            y = current_laser.getY1()
            x2 = current_laser.getX2()
            y2 = current_laser.getY2()
            lenAB = math.sqrt(pow(x - x2, 2.0) + pow(y - y2, 2.0))
            x3 = int(x2 + (x2 - x) / lenAB * 10000)
            y3 = int(y2 + (y2 - y) / lenAB * 10000)
            point = (x3, y3)
            finalPointList.append(point)


        # Manages the break statement
        # breaking = False
        # for i in range(len(mirrorBLockerList)):
        #     if i is not prevReflect:
        #         if colBool[i] is True:
        #             breaking = False
        #             break
        #         else:
        #             breaking = True
        if breaking is True:
            break

        # if counter > 10:
        #     break
        # counter += 1

    # While loops ends here ------------------------------

    #print('hey')
    # Draws the lasers from a list of points.
    return_arrayList = []
    for i in range(len(finalPointList)-1):
        if i is 3:
            color = (255, 0, 0)
            weight = 10
        else:
            color = (0, 255, 0)
            weight = 5
        cv2.line(img, finalPointList[i], finalPointList[i+1], color, weight)
        x, y = finalPointList[i]
        x2, y2 = finalPointList[i+1]
        temp_laser = Laser.Laser(x, y, x2, y2, img)
        return_arrayList.append(temp_laser)
    return return_arrayList

    # draws the lasers from a list of laser.
    #finalLaser.drawLaser()
    #for i in range(len(finalLaserList)):
     #   finalLaserList[i].drawLaser()



cap = cv2.VideoCapture(0)

ret, last_frame = cap.read()

if last_frame is None:
    exit()

while(cap.isOpened()):
    ret, frame = cap.read()

    if frame is None:
        exit()

    lasers = laserFire(frame,20,0.2) #Call to laser function
    print(lasers)
    cv2.imshow('frame', frame)
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window", img)



    if cv2.waitKey(33) >= 0:
        break

    last_frame = frame

cap.release()
cv2.destroyAllWindows()

# tempVectorX = tempLaser.getX2 - tempLaser.getX1
#
# tempVectorY = tempLaser.getY2 - tempLaser.getY1
#
# if tempVectorX > 0 and tempVectorY > 0:
#     #do stuff to but right laser
# elif tempVectorX < 0 and tempVectorY < 0:
#     #do some other stuff
# elif tempVectorX < 0 and tempVectorY > 0:
#     #do stuff
# elif tempVectorX > 0 and tempVectorY < 0:
#     #last stuff to do
# else:
#     #Do other stuff just incase
