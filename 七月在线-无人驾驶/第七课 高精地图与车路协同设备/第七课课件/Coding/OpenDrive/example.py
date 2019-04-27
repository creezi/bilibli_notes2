from lxml import etree
from opendriveparser import parse_opendrive
import matplotlib.pyplot as plt
import numpy as np
import math

fh = open("./Crossing8Course.xodr", 'r')
openDrive = parse_opendrive(etree.parse(fh).getroot())
fh.close()

precision = 0.5
fig = plt.figure()

for road in openDrive.roads:
    print("Road ID: {}".format(road.id))
    
    plan_view = road.planView
    length = plan_view.getLength()

    left_lane = []
    right_lane = []
    for lane_section in road.lanes.laneSections:
        for llane in lane_section.leftLanes:
            if llane.type == "driving":
                left_lane.append(llane)
        for rlane in lane_section.rightLanes:
            if rlane.type == "driving":
                right_lane.append(rlane)

    ref_pos_x = []
    ref_pos_y = []
    ref_heading = []
    left_pos_x = []
    left_pos_y = []
    right_pos_x = []
    right_pos_y = []

    numSteps = max(2, np.ceil(length / float(precision)))
    for s in np.linspace(0, length, int(numSteps)):
        pos, tangent = plan_view.calc(s)

        ref_pos_x.append(pos[0])
        ref_pos_y.append(pos[1])
        ref_heading.append(tangent)

        distance = 0
        for llane in left_lane:
            for width in llane.widths:
                distance = np.polynomial.polynomial.polyval(s - width.sOffset, width.coeffs)

        ortho = tangent + np.pi / 2
        new_pos = pos + np.array([distance * np.cos(ortho), distance * np.sin(ortho)])
        left_pos_x.append(new_pos[0])
        left_pos_y.append(new_pos[1])

        distance = 0
        for rlane in right_lane:
            for width in rlane.widths:
                distance = np.polynomial.polynomial.polyval(s - width.sOffset, width.coeffs)

        ortho = tangent - np.pi / 2
        new_pos = pos + np.array([distance * np.cos(ortho), distance * np.sin(ortho)])
        right_pos_x.append(new_pos[0])
        right_pos_y.append(new_pos[1])


    plt.plot(ref_pos_x, ref_pos_y, 'k--', linewidth=0.5)
    plt.plot(right_pos_x, right_pos_y, 'r', linewidth=1.0)
    plt.plot(left_pos_x, left_pos_y, 'r', linewidth=1.0)

plt.show()
