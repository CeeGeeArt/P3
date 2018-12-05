import Mirror
import Collision
import Laser
import Blocker
import math
import cv2
#import Queue


#img = cv2.imread('test.jpg')
#height, width, channels = img.shape

def laserFire(laser_start, totLaserPos, timePerPos, mirrorBlockerList, img):
    print('____________________________________________________________________________________________')
    # ------ Mirrors and blockers must have their points input in a counter clockwise manner. -----
    #
    # testBlock = Blocker.Blocker(320, 100, 299, 290, 200, 290, 200, 100, img)
    #
    # #testBlocker = Mirror.Mirror(500, 125, 550, 900, 700, 900, 700, 125, img)
    # testBlocker = Mirror.Mirror(700, 125, 700, 900, 550, 900, 500, 125, img)
    #
    # testBlock1 = Mirror.Mirror(190, 350, 199, 900, 180, 900, 180, 350, img)
    #
    # testBlock2 = Mirror.Mirror(151, 450, 150, 950, 130, 950, 130, 450, img)
    #
    # #testBlock3 = Mirror.Mirror(240, 500, 242, 950, 400, 950, 500, 500, img)
    # testBlock3 = Mirror.Mirror(500, 500, 400, 950, 242, 950, 240, 699, img)
    #
    # #testBlocker2 = Mirror.Mirror(100, height-50, 100, height, 900, height, 900, height-150, img)
    # testBlocker2 = Mirror.Mirror(900, height - 170, 900, height, 100, height, 100, height - 50, img)
    #
    # #testBlocker3 = Mirror.Mirror(720, 90, 680, 300, 625, 300, 600, 50, img)
    # #testBlocker4 = Mirror.Mirror(900, 50, 860, 300, 800, 300, 800, 50, img)
    # #testBlocker2 = Blocker.Blocker(-5, -5, -5, height+5, width+5, height+5, width+5, -5, img)
    #
    # mirrorBlockerList = [testBlock, testBlocker, testBlock1, testBlock2, testBlock3, testBlocker2]
    # mirrorBlockerList.append(testBlock)

    # Add start point to the point list
    lsX = laser_start.getX1()
    lsY = laser_start.getY1()
    finalLaser = None
    finalPointList = [(lsX, lsY)]
    prevReflect = None
    newReflect = None
    newBlocked = None
    x3 = None
    y3 = None
    counter = 0

    # current_laser = Laser.Laser(lsX, lsY, leX, leY)
    current_laser = laser_start
    print("start while loop --------------------------------------------")
    while True:
        currentReflect = []
        currentBlocked = []
        prevReflect = newReflect
        prevBlocked = newBlocked
        colBool = []
        colBoolBlocker = []
        tempLaser = None
        reflectArray = []
        reflectArray2 = []
        blockedArray = []
        blockedArray2 = []
        blockStop = False

        print("start for loops______________________________________________________-")
        for i in range(len(mirrorBlockerList)):
            colBool.append(True)
            colBoolBlocker.append(True)

        compareLaser = current_laser
        # print("Compare laser:")
        # print(compareLaser.getX1(), compareLaser.getY1(), compareLaser.getX2(), compareLaser.getY2())
        for j in range(len(mirrorBlockerList)):
            # print(mirrorBlockerList[j].getRectangleX1(), mirrorBlockerList[j].getRectangleY1())
            # print(mirrorBlockerList[j].getRectangleX2(), mirrorBlockerList[j].getRectangleY2())
            # print(mirrorBlockerList[j].getRectangleX3(), mirrorBlockerList[j].getRectangleY3())
            # print(mirrorBlockerList[j].getRectangleX4(), mirrorBlockerList[j].getRectangleY4())

            col = Collision.Collision(mirrorBlockerList[j], compareLaser)
            tempLaser = col.collisionDetection(img)
            # print(tempLaser.getX1())
            colBool[j] = col.reflected
            colBoolBlocker[j] = col.blocked
            # print(colBoolBlocker)
            # print(colBool)

            if colBool[j] is True and j is not prevReflect:
                x = tempLaser.getX1()
                y = tempLaser.getY1()
                point = (x, y)
                reflectArray.append(point)
                end_x = tempLaser.getX2()
                end_y = tempLaser.getY2()
                end_point = (end_x, end_y)
                reflectArray2.append(end_point)
                currentReflect.append(j)
            elif colBoolBlocker[j] is True and j is not prevBlocked:
                x = tempLaser.getX1()
                y = tempLaser.getY1()
                point = (x, y)
                blockedArray.append(point)
                #print(len(blockedArray))
                end_x = tempLaser.getX2()
                end_y = tempLaser.getY2()
                end_point = (end_x, end_y)
                blockedArray2.append(end_point)
                currentBlocked.append(j)


            # if counter > 4:
            #     if j is 2:
            #         print(tempLaser.getX1(), tempLaser.getY1())
            #         print(colBool[j])
            #     print("in loop info")
            #     print(prevReflect)
            #     print(currentReflect)
            #     print(reflectArray)
            #     print("in loop stop")

            # print("j = " + str(j))
            # print(colBool[j])

        # print("reflectArray: " + str(reflectArray))
        # print(blockStop)
        # Remove point from the reflectArray that are placed in the wrong direction.
        real_direction_x = current_laser.getX2() - current_laser.getX1()
        real_direction_y = current_laser.getY2() - current_laser.getY1()
        # print(real_direction_x, real_direction_y)
        compare_x = []
        compare_y = []
        block_compare_x = []
        block_compare_y = []
        popArray = []
        blocker_popArray = []
        for i in range(len(reflectArray)):
            compare_x.append(reflectArray[i][0])
            compare_y.append(reflectArray[i][1])
            new_direction_x = compare_x[i] - current_laser.getX1()
            new_direction_y = compare_y[i] - current_laser.getY1()
            #print(real_direction_x)
            #print(current_laser.getX1())
            #print(compare_x)
            #print(new_direction_x)

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
                if not (new_direction_x == 0):
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
                if not (new_direction_y == 0):
                    popArray.append(i)

        for i in range(len(blockedArray)):
            block_compare_x.append(blockedArray2[i][0])
            block_compare_y.append(blockedArray2[i][1])
            # print(block_compare_x[i])
            # print(current_laser.getX1())
            # print(block_compare_y)
            # print(current_laser.getY1())
            blocker_new_direction_x = current_laser.getX1() - block_compare_x[i]
            blocker_new_direction_y = current_laser.getY1() - block_compare_y[i]
            # print('In this SHIIT')
            # print(blocker_new_direction_x, blocker_new_direction_y)
            # print('real')
            # print(real_direction_x, real_direction_y)
            #print(real_direction_x)
            #print(current_laser.getX1())
            #print(block_compare_x)
            #print(blocker_new_direction_x)

        #     # Marks an entry for removal if the direction does not match with the known direction.
        #     # Checks x-axis
            if real_direction_x < 0:
                # Check
                if not (blocker_new_direction_x > 0):
                    blocker_popArray.append(i)
                    continue
            elif real_direction_x > 0:
                # check
                if not (blocker_new_direction_x < 0):
                    blocker_popArray.append(i)
                    continue
            else:
                # Direction = 0
                if not (blocker_new_direction_x == 0):
                    blocker_popArray.append(i)
                    continue
        #
            # Checks y-axis
            if real_direction_y < 0:
                # Check
                if not (blocker_new_direction_y > 0):
                    blocker_popArray.append(i)
            elif real_direction_y > 0:
                # check
                if not (blocker_new_direction_y < 0):
                    blocker_popArray.append(i)
            else:
                # Direction = 0
                if not (blocker_new_direction_y == 0):
                    blocker_popArray.append(i)

        # Pops entries based on the markings. Reverse sorted to prevent interference with later iterations.
        # print('popArrayA')
        # print(len(popArray))
        # print('popArrayB')
        # print(len(blockedArray))
        # print(blockedArray)
        # print(len(blocker_popArray))
        popArray.sort(reverse=True)
        blocker_popArray.sort(reverse=True)
        # print(blocker_popArray)
        # print(reflectArray)
        for i in range(len(popArray)):
            reflectArray.pop(popArray[i])
            reflectArray2.pop(popArray[i])
            currentReflect.pop(popArray[i])

        for i in range(len(blocker_popArray)):
            blockedArray.pop(blocker_popArray[i])
            blockedArray2.pop(blocker_popArray[i])
            currentBlocked.pop(blocker_popArray[i])
            # print('Bam')
        # print(reflectArray)
        # print("start point: " + str(finalPointList[len(finalPointList)-1]))

        breaking = False
        # print(blockedArray)
        # print(len(blockedArray))
        # Check which laser is the shortest
        # print("start compare loop")
        startX, startY = finalPointList[len(finalPointList) - 1]
        compare = (0,0)
        ekstra_compare = (0,0)
        compareBlocker = (0,0)
        ekstra_compareBlocker = (0,0)

        shortestBlockerStart = (0,0)
        shortestBlockerEnd = (0,0)
        shortestReflectedStart = (0,0)
        shortestReflectedEnd = (0,0)

        #Bring disse sammen, så den som standard syntes at der er en af hver, og inde i det rent faktisk tjekker om der er
        #Hvis ikke så kør alene kode, hvis der er kør distance tjek sammen, og tjek om den tættest på er mirror eller blocker
        #Kør der efter rigtig kode på disse.
        print('!"#¤%&/()/&%¤#"!!#¤%&/(/&%¤#"!§!#"¤%&/()(&/%¤#"!"¤#%&/(/)(&%¤#"!"¤#%&/(&/%¤#"#%¤&/()(&/%¤#"¤#%&/(')
        print(len(reflectArray))
        print(len(blockedArray))
        # More than 1 of one
        if (len(reflectArray) >= 1 and len(blockedArray) > 1) or (len(reflectArray) > 1 and len(blockedArray) >= 1):
            print('Both on Screeee,!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')



            if len(reflectArray) > 1:
                # print("BBC")
                for i in range(len(reflectArray) - 1):
                    x, y = reflectArray[i]
                    x2, y2 = reflectArray[i + 1]
                    if i is 0:
                        # Find the closest of the first two points in the array.
                        distanceToPoint1 = math.sqrt(((startX - x) ** 2) + ((startY - y) ** 2))
                        distanceToPoint2 = math.sqrt(((startX - x2) ** 2) + ((startY - y2) ** 2))
                        if distanceToPoint1 < distanceToPoint2:
                            compare = reflectArray[i]
                            ekstra_compare = reflectArray2[i]
                            newReflect = currentReflect[i]
                        else:
                            compare = reflectArray[i + 1]
                            ekstra_compare = reflectArray2[i + 1]
                            newReflect = currentReflect[i + 1]
                    else:
                        # Compare the previously closest point to the next entry in the array.
                        x, y = compare
                        distanceToPoint1 = math.sqrt(((startX - x) ** 2) + ((startY - y) ** 2))
                        distanceToPoint2 = math.sqrt(((startX - x2) ** 2) + ((startY - y2) ** 2))
                        if distanceToPoint1 > distanceToPoint2:
                            compare = reflectArray[i + 1]
                            ekstra_compare = reflectArray2[i + 1]
                            newReflect = currentReflect[i + 1]

            elif len(reflectArray) > 0:
                # print("BBB")
                compare = reflectArray[0]
                ekstra_compare = reflectArray2[0]

            if len(blockedArray2) > 1:
                for i in range(len(blockedArray2) - 1):
                    x, y = blockedArray2[i]
                    x2, y2 = blockedArray2[i + 1]
                    if i is 0:
                        # Find the closest of the first two points in the array.
                        distanceToPoint1 = math.sqrt(((startX - x) ** 2) + ((startY - y) ** 2))
                        distanceToPoint2 = math.sqrt(((startX - x2) ** 2) + ((startY - y2) ** 2))
                        if distanceToPoint1 < distanceToPoint2:
                            compareBlocker = blockedArray2[i]
                        else:
                            compareBlocker = blockedArray2[i + 1]
                    else:
                        # Compare the previously closest point to the next entry in the array.
                        x, y = compareBlocker
                        distanceToPoint1 = math.sqrt(((startX - x) ** 2) + ((startY - y) ** 2))
                        distanceToPoint2 = math.sqrt(((startX - x2) ** 2) + ((startY - y2) ** 2))
                        if distanceToPoint1 > distanceToPoint2:
                            compareBlocker = blockedArray2[i + 1]

            elif len(blockedArray2) > 0:
                # print("BBB")
                compareBlocker = blockedArray2[0]

            if compare[0] is not 0 and compareBlocker[0] is not 0:
                blockerX1, blockerY1 = compareBlocker

                reflectedX1, reflectedY1 = compare

                distanceToPoint1 = math.sqrt(((startX - blockerX1) ** 2) + ((startY - blockerY1) ** 2))
                distanceToPoint2 = math.sqrt(((startX - reflectedX1) ** 2) + ((startY - reflectedY1) ** 2))

                if distanceToPoint1 < distanceToPoint2:
                    print('blocker_________________________________________________')
                    finalPointList.append(compareBlocker)
                    x, y = compareBlocker
                    point = x, y
                    finalPointList.append(point)
                    breaking = True
                elif distanceToPoint1 > distanceToPoint2:
                    print('mirror___________________________________________________')
                    finalPointList.append(compare)
                    newReflect = currentReflect
                    x, y = compare
                    x2, y2 = ekstra_compare
                    current_laser = Laser.Laser(x, y, x2, y2)

        # One of each
        elif len(reflectArray) == 1 == len(blockedArray):
            blockerX2, blockerY2 = blockedArray2[0]
            reflectedX1, reflectedY1 = reflectArray[0]

            distanceToPoint1 = math.sqrt(((startX - blockerX2) ** 2) + ((startY - blockerY2) ** 2))
            distanceToPoint2 = math.sqrt(((startX - reflectedX1) ** 2) + ((startY - reflectedY1) ** 2))

            if distanceToPoint1 < distanceToPoint2:
                print('blocker_________________________________________________')
                finalPointList.append(blockedArray[0])
                x, y = blockedArray[0]
                x2, y2 = blockedArray2[0]
                current_laser = Laser.Laser(x, y, x2, y2)
                point = x2, y2
                finalPointList.append(point)
                breaking = True
            elif distanceToPoint1 > distanceToPoint2:
                print('mirror___________________________________________________')
                finalPointList.append(reflectArray[0])
                newReflect = currentReflect
                x, y = reflectArray[0]
                x2, y2 = reflectArray2[0]
                current_laser = Laser.Laser(x, y, x2, y2)

        # Only mirrors
        elif len(reflectArray) > 0 and len(blockedArray) == 0:
            print("B")
            if len(reflectArray) > 1:
                # print("BBC")
                for i in range(len(reflectArray) - 1):
                    x, y = reflectArray[i]
                    x2, y2 = reflectArray[i + 1]
                    if i is 0:
                        # Find the closest of the first two points in the array.
                        distanceToPoint1 = math.sqrt(((startX - x) ** 2) + ((startY - y) ** 2))
                        distanceToPoint2 = math.sqrt(((startX - x2) ** 2) + ((startY - y2) ** 2))
                        if distanceToPoint1 < distanceToPoint2:
                            compare = reflectArray[i]
                            ekstra_compare = reflectArray2[i]
                            newReflect = currentReflect[i]
                        else:
                            compare = reflectArray[i + 1]
                            ekstra_compare = reflectArray2[i + 1]
                            newReflect = currentReflect[i + 1]
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
                current_laser = Laser.Laser(x, y, x2, y2)

            elif len(reflectArray) > 0:
                # print("BBB")
                finalPointList.append(reflectArray[0])
                newReflect = currentReflect[0]
                x, y = reflectArray[0]
                x2, y2 = reflectArray2[0]
                current_laser = Laser.Laser(x, y, x2, y2)

        # Only blockers
        elif len(blockedArray2) > 0 == len(reflectArray):
            print("BBB")

            if len(blockedArray2) > 1:
                for i in range(len(blockedArray2) - 1):
                    x, y = blockedArray2[i]
                    x2, y2 = blockedArray2[i + 1]
                    print(x)
                    print(x2)
                    if i is 0:
                        # Find the closest of the first two points in the array.
                        distanceToPoint1 = math.sqrt(((startX - x) ** 2) + ((startY - y) ** 2))
                        distanceToPoint2 = math.sqrt(((startX - x2) ** 2) + ((startY - y2) ** 2))
                        if distanceToPoint1 < distanceToPoint2:
                            compare = blockedArray2[i]
                        else:
                            compare = blockedArray2[i + 1]
                    else:
                        # Compare the previously closest point to the next entry in the array.
                        x, y = compare
                        distanceToPoint1 = math.sqrt(((startX - x) ** 2) + ((startY - y) ** 2))
                        distanceToPoint2 = math.sqrt(((startX - x2) ** 2) + ((startY - y2) ** 2))
                        if distanceToPoint1 > distanceToPoint2:
                            compare = blockedArray2[i + 1]
                finalPointList.append(compare)
                breaking = True

            elif len(blockedArray2) > 0:
                # print("BBB")
                finalPointList.append(blockedArray2[0])
                breaking = True

        # No blocker or mirror
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
            block_point = None
            finalPointList.append(point)

            # last_compare = Laser.Laser(x, y, x3, y3)
            # for i in range(len(mirrorBlockerList)):
            #     col = Collision.Collision(mirrorBlockerList[i], last_compare)
            #     tempLaser = col.collisionDetection(img)
            #     if col.blocked is True:
            #         x = tempLaser.getX2()
            #         y = tempLaser.getY2()
            #         block_point = x, y
            #         blockStop = col.blocked
            #
            # if blockStop is True:
            #     finalPointList.append(block_point)
            # else:
            #     finalPointList.append(point)



        # Manages the break statement
        counter += 1
        if 50 < counter:
            breaking = True


        if breaking is True:
            break

    # While loops ends here ------------------------------

    # Draws the lasers from a list of points.
    return_arrayList = []
    for i in range(len(finalPointList)-1):
        if i is 3:
            color = (255, 0, 0)
            weight = 10
        else:
            color = (0, 255, 0)
            weight = 5
        #cv2.line(img, finalPointList[i], finalPointList[i+1], color, weight)
        x, y = finalPointList[i]
        x2, y2 = finalPointList[i+1]
        temp_laser = Laser.Laser(x, y, x2, y2)
        return_arrayList.append(temp_laser)
    return return_arrayList, img



# cap = cv2.VideoCapture(0)
#
# ret, last_frame = cap.read()
#
# if last_frame is None:
#     exit()
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#
#     if frame is None:
#         exit()
#
#     lasers = laserFire(frame,20,0.2) #Call to laser function
#     print(lasers)
#     cv2.imshow('frame', frame)
#     cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
#     cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#     cv2.imshow("window", img)
#
#
#
#     if cv2.waitKey(33) >= 0:
#         break
#
#     last_frame = frame
#
# cap.release()
# cv2.destroyAllWindows()
