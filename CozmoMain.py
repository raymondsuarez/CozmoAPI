#!/usr/bin/env python
# Code samples for Ryan from Ray

import cozmo
from tkinter import Tk, ttk
from tkinter import messagebox
from cozmo.util import degrees, distance_mm, speed_mmps
import MultiColumnLB as mclb


#Global Variables
cozmo_commands = ('drive_straight', 'say_text', 'turn_left', 'turn_right', 'count', 'drive_square', 'seven', 'eight', 'nine', 'ten')
drive_straight_PV = {'distance_mm': 150, 'speed_mmps': 50 }
turn_left_PV = {'degrees': 90, 'speed_mmps': 50 }
turn_right_PV = {'degrees': -90, 'speed_mmps': 50 }

drive_straight_values = (11, 23, 54)
run_list = ('drive_straight', 'say_text')

sayTextVars = ('string')
turnInPlaceVars = ('degrees')


#Start Functions...
def cozmo_drive_straight(robot: cozmo.robot.Robot):
    # Move and take a left
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

def cozmo_left_turn(robot: cozmo.robot.Robot):
    # Move and take a left
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

def cozmo_right_turn(robot: cozmo.robot.Robot):
    # Move and take a left
    robot.turn_in_place(degrees(-90)).wait_for_completed()

def cozmo_count(robot: cozmo.robot.Robot):
    # Voice Count to 3
    for i in range(3):
        robot.say_text(str(i + 1)).wait_for_completed()

def cozmo_talk(robot: cozmo.robot.Robot):
    # First words Ryan :-)
    robot.say_text("Hello Ryan").wait_for_completed()

def cozmo_drive_square(robot: cozmo.robot.Robot):
    # Make a small square
    for _ in range(4):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()

def on_select(option):
        print("Option", option)
        if option == ['say_text']:
            cozmo.run_program(cozmo_talk)
            print("Talk Complete", option)
        elif option == ['turn_left']:
            cozmo.run_program(cozmo_left_turn)
            print("Left Complete", option)
        elif option == ['turn_right']:
            cozmo.run_program(cozmo_right_turn)
            print("Right Complete", option)
        elif option == ['drive_straight']:
            cozmo.run_program(cozmo_drive_straight)
            print("Straight Complete", option)
        elif option == ['drive_square']:
            cozmo.run_program(cozmo_drive_square)
            print("Square Complete", option)
        print("\n")


def show_info(msg):
    messagebox.showinfo("Table Data", msg)



def main():
    #Create mainwindow and frames.
    root = Tk()
    root.title("Cozmo Controler")
    root.geometry("850x300+200+200")

    topframe = ttk.Frame(root)#, padx=3, pady=3)
    topframe.pack( side ="top", padx=5, pady=10)

    bottomframe = ttk.Frame(root)#, padx=3, pady=3)
    bottomframe.pack( side ="bottom", padx=5, pady=10)

    #Add widgets to the correct frames()

    addBT = ttk.Button(topframe, text="Add to Run List")
    addBT.pack( side = "left", padx=5, pady=10 )

    runBT = ttk.Button(topframe, text="Run the List")
    runBT.pack( side = "left", padx=5, pady=10 )

    deleteBT = ttk.Button(topframe, text="Delete from Run List" )
    deleteBT.pack( side = "left", padx=5, pady=10 )

    quitBT = ttk.Button(topframe, text="Quit", command=exit)
    quitBT.pack( side = "right", padx=200, pady=10 )

    commandLB = mclb.Multicolumn_Listbox(bottomframe, ["Cozmo Command"], stripped_rows=("#D4E6F1", "#A9CCE3"), command=on_select, )
    commandLB.interior.pack( side="left", padx=5, pady=10)

    propatribLB = mclb.Multicolumn_Listbox(bottomframe, ["Property", "Value"], stripped_rows=("#D4E6F1", "#A9CCE3"), command=on_select)
    propatribLB.interior.pack( side = "left", padx=5, pady=10 )

    runcommandLB = mclb.Multicolumn_Listbox(bottomframe, ["Run List"], stripped_rows=("#D4E6F1", "#A9CCE3"), command=on_select)
    runcommandLB.interior.pack( side = "left", padx=5, pady=10 )


# Initialize Cozmo Command list
    commandLB.clear()
    for i in range(len(cozmo_commands)):
        commandLB.insert_row([" "])
        commandLB.column[0] = cozmo_commands
    commandLB.select_row(0)


# Initialize Property and Attribute list
    propatribLB.clear()
    prop_string = list(drive_straight_PV.keys())
    value_string = list(drive_straight_PV.values())
    for i in range(len(prop_string)):
        propatribLB.insert_row([" ", " "])
        propatribLB.column[0] = prop_string
        propatribLB.column[1] = value_string
    propatribLB.select_row(0)


# Initialize Run Command list
    runcommandLB.clear()
    for i in range(len(run_list)):
        runcommandLB.insert_row([" "])
        runcommandLB.column[0] = run_list

    root.mainloop()


if __name__ == "__main__":
    main()