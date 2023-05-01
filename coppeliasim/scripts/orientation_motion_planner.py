#python

import math
import numpy as np
maxVel = [0.25,0.125]
maxAccel = [0.25, 0.125]


def sysCall_thread():
    # e.g. non-synchronized loop:
    sim.setThreadAutomaticSwitch(True)
    print(f'threaded script')
    sim.addLog(0,"threaded script")
    goal = sim.getObject("/target")
    print(f'goal: {goal}')
    dt = sim.getSimulationTimeStep() * 2.0
    print(f'dt: {dt}')
    while True:
        pathHandle = sim.getInt32Signal('pathHandle')
        if pathHandle:
            sim.clearInt32Signal('pathHandle')
            path_data = sim.readCustomDataBlock(pathHandle, 'PATH')
            path=sim.unpackDoubleTable(path_data)
            pathMat = np.array(path).reshape(len(path) // 7, 7)
            count = 0
            while count < len(pathMat) - 1:  # Stop at the second last pose to avoid IndexError
                current_pose = pathMat[count]
                next_pose = pathMat[count + 1]
                # Calculate the desired orientation for the robot based on the direction to the next pose
                desired_orientation = calculate_orientation(current_pose[:3], next_pose[:3])
                # Set the robot's position and orientation
                sim.setObjectPosition(goal, -1, current_pose[:3].tolist())
                sim.setObjectOrientation(goal, -1, desired_orientation)
                sim.wait(dt)
                count += 1
            # Set the final pose without changing the orientation (optional)
            sim.setObjectPosition(goal, -1, pathMat[-1][:3].tolist())
            sim.wait(dt)


def calculate_orientation(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    yaw = math.atan2(dy, dx)
    # Assuming the robot moves on a 2D plane (X, Y) with a fixed Z-axis orientation
    return [0, 0, yaw]