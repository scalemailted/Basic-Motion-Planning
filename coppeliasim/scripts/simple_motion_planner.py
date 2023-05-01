#python

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
            while count < len(pathMat):
                pose = pathMat[count]
                count += 1
                sim.setObjectPosition(goal, -1, pose[:3].tolist())
                sim.setObjectQuaternion(goal, -1, pose[3:].tolist())
                sim.wait(dt)