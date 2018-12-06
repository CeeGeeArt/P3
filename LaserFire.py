import Collision
import Laser
import math


def laserFire(laser_start, totLaserPos, timePerPos, mirrorBlockerList, img):
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

    current_laser = laser_start
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

        for i in range(len(mirrorBlockerList)):
            colBool.append(True)
            colBoolBlocker.append(True)

        compareLaser = current_laser
        for j in range(len(mirrorBlockerList)):
            col = Collision.Collision(mirrorBlockerList[j], compareLaser)
            tempLaser = col.collisionDetection(img)
            colBool[j] = col.reflected
            colBoolBlocker[j] = col.blocked

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
                end_x = tempLaser.getX2()
                end_y = tempLaser.getY2()
                end_point = (end_x, end_y)
                blockedArray2.append(end_point)
                currentBlocked.append(j)

        real_direction_x = current_laser.getX2() - current_laser.getX1()
        real_direction_y = current_laser.getY2() - current_laser.getY1()
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
            blocker_new_direction_x = current_laser.getX1() - block_compare_x[i]
            blocker_new_direction_y = current_laser.getY1() - block_compare_y[i]

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
        popArray.sort(reverse=True)
        blocker_popArray.sort(reverse=True)
        for i in range(len(popArray)):
            reflectArray.pop(popArray[i])
            reflectArray2.pop(popArray[i])
            currentReflect.pop(popArray[i])

        for i in range(len(blocker_popArray)):
            blockedArray.pop(blocker_popArray[i])
            blockedArray2.pop(blocker_popArray[i])
            currentBlocked.pop(blocker_popArray[i])

        breaking = False
        # Check which laser is the shortest
        startX, startY = finalPointList[len(finalPointList) - 1]
        compare = (0,0)
        ekstra_compare = (0,0)
        compareBlocker = (0,0)
        ekstra_compareBlocker = (0,0)

        # More than 1 of one
        if (len(reflectArray) >= 1 and len(blockedArray) > 1) or (len(reflectArray) > 1 and len(blockedArray) >= 1):
            print('Both on Screeee,!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

            # If more than one mirror
            if len(reflectArray) > 1:
                print("ra2+")
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

            # If only one mirror
            elif len(reflectArray) > 0:
                print("ra1")
                compare = reflectArray[0]
                ekstra_compare = reflectArray2[0]

            # If more than one blocker
            if len(blockedArray2) > 1:
                print("ba2+")
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
            # If only one blocker
            elif len(blockedArray2) > 0:
                print("Ba1")
                compareBlocker = blockedArray2[0]

            # Compares the distance of the mirrors and blockers and finds the shortest one
            if compare[0] is not 0 and compareBlocker[0] is not 0:
                blockerX1, blockerY1 = compareBlocker

                reflectedX1, reflectedY1 = compare

                distanceToPoint1 = math.sqrt(((startX - blockerX1) ** 2) + ((startY - blockerY1) ** 2))
                distanceToPoint2 = math.sqrt(((startX - reflectedX1) ** 2) + ((startY - reflectedY1) ** 2))

                # Blocker is closest
                if distanceToPoint1 < distanceToPoint2:
                    print('blocker_________________________________________________')
                    finalPointList.append(compareBlocker)
                    x, y = compareBlocker
                    point = x, y
                    finalPointList.append(point)
                    breaking = True

                # Mirror is closest
                elif distanceToPoint1 > distanceToPoint2:
                    print('mirror___________________________________________________')
                    finalPointList.append(compare)
                    newReflect = currentReflect
                    x, y = compare
                    x2, y2 = ekstra_compare
                    current_laser = Laser.Laser(x, y, x2, y2)

        # One of each
        elif len(reflectArray) == 1 == len(blockedArray):
            print("one of each")
            blockerX2, blockerY2 = blockedArray2[0]
            reflectedX1, reflectedY1 = reflectArray[0]

            distanceToPoint1 = math.sqrt(((startX - blockerX2) ** 2) + ((startY - blockerY2) ** 2))
            distanceToPoint2 = math.sqrt(((startX - reflectedX1) ** 2) + ((startY - reflectedY1) ** 2))

            # Blocker is closest
            if distanceToPoint1 < distanceToPoint2:
                print('blocker_________________________________________________')
                finalPointList.append(blockedArray[0])
                x, y = blockedArray[0]
                x2, y2 = blockedArray2[0]
                current_laser = Laser.Laser(x, y, x2, y2)
                point = x2, y2
                finalPointList.append(point)
                breaking = True

            # Mirror is closest
            elif distanceToPoint1 > distanceToPoint2:
                print('mirror___________________________________________________')
                finalPointList.append(reflectArray[0])
                newReflect = currentReflect
                x, y = reflectArray[0]
                x2, y2 = reflectArray2[0]
                current_laser = Laser.Laser(x, y, x2, y2)

        # Only mirrors
        elif len(reflectArray) > 0 and len(blockedArray) == 0:
            # If more than one mirror
            if len(reflectArray) > 1:
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
                # Updates the laser based on shortest point
                finalPointList.append(compare)
                x, y = compare
                x2, y2 = ekstra_compare
                current_laser = Laser.Laser(x, y, x2, y2)

            # If only one mirror
            elif len(reflectArray) > 0:
                print("BBB")
                finalPointList.append(reflectArray[0])
                newReflect = currentReflect[0]
                x, y = reflectArray[0]
                x2, y2 = reflectArray2[0]
                current_laser = Laser.Laser(x, y, x2, y2)

        # Only blockers
        elif len(blockedArray2) > 0 == len(reflectArray):
            # More than one blocker
            if len(blockedArray2) > 1:
                for i in range(len(blockedArray2) - 1):
                    x, y = blockedArray2[i]
                    x2, y2 = blockedArray2[i + 1]
                    # print(x)
                    # print(x2)
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

            # Only one blocker
            elif len(blockedArray2) > 0:
                # print("BBB")
                finalPointList.append(blockedArray2[0])
                breaking = True

        # No blocker or mirror
        else:
            breaking = True
            x = current_laser.getX1()
            y = current_laser.getY1()
            x2 = current_laser.getX2()
            y2 = current_laser.getY2()

            # Extends the laser so it goes beyond the screen.
            lenAB = math.sqrt(pow(x - x2, 2.0) + pow(y - y2, 2.0))
            x3 = int(x2 + (x2 - x) / lenAB * 10000)
            y3 = int(y2 + (y2 - y) / lenAB * 10000)
            point = (x3, y3)
            finalPointList.append(point)

        # Manages the break statement
        counter += 1
        if 50 < counter:
            breaking = True

        if breaking is True:
            break

    # While loops ends here ------------------------------

    # Draws the lasers from a list of points.
    return_arrayList = []
    print(len(finalPointList))
    for i in range(len(finalPointList)-1):
        x, y = finalPointList[i]
        x2, y2 = finalPointList[i+1]
        temp_laser = Laser.Laser(x, y, x2, y2)
        return_arrayList.append(temp_laser)
        print(len(return_arrayList))
    return return_arrayList, img
