#!/usr/bin/python3

#Code samples for Ryan from Ray

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_talk(robot: cozmo.robot.Robot):
    #First words Ryan :-)
    robot.say_text("Hello Ryan").wait_for_completed()


def cozmo_left_turn(robot: cozmo.robot.Robot):
    #Move and take a left
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()


def cozmo_count(robot: cozmo.robot.Robot):
    #Voice Count to 3
    for i in range(3):
        robot.say_text(str(i+1)).wait_for_completed()


def cozmo_drive_square(robot: cozmo.robot.Robot):
    #Make a small square
    for _ in range(4):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()



option = 1
while option != 0:
    print('Setting up result')
    print("1. Make Cozmo talk")
    print("2. Move - straight:left:straight")
    print("3. Make Cozmo count")
    print("4. Move - small square")
    print(" ")
    print("0. Exit")
    option = int(input('Select a Number\n'))
    print("Option", option)
    if option == 1:
        cozmo.run_program(cozmo_talk);
    elif option == 2:
        cozmo.run_program(cozmo_left_turn);
    elif option == 3:
        cozmo.run_program(cozmo_count);
    elif option == 4:
        cozmo.run_program(cozmo_drive_square);


