#!/usr/bin/env python
# Code samples for Ryan from Ray

import cozmo
from tkinter import Tk, ttk
from tkinter import messagebox
from cozmo.util import degrees, distance_mm, speed_mmps
import MultiColumnLB as mclb


#Global Variables
cozmoCommands = ('drive_straight', 'say_text', 'turn_in_place', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
driveStraightVars = ('distance','speed')
sayTextVars = ('string')
turnInPlaceVars = ('degrees')







def cozmo_talk(robot: cozmo.robot.Robot):
    # First words Ryan :-)
    robot.say_text("Hello Ryan").wait_for_completed()


def cozmo_left_turn(robot: cozmo.robot.Robot):
    # Move and take a left
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()


def cozmo_count(robot: cozmo.robot.Robot):
    # Voice Count to 3
    for i in range(3):
        robot.say_text(str(i + 1)).wait_for_completed()


def cozmo_drive_square(robot: cozmo.robot.Robot):
    # Make a small square
    for _ in range(4):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()

def on_select(data):
        print("called command when row is selected")
        print(data)
        print("\n")


def show_info(msg):
    messagebox.showinfo("Table Data", msg)




def main():
    #Create mainwindow and frame.
    root = Tk()
    root.title("Cozmo Controler")
    root.geometry("800x300+200+200")

    # layout all of the main containers
 #   root.grid_rowconfigure(1, weight=1)
 #   root.grid_columnconfigure(0, weight=1)
#    top_frame = ttk.Frame(root, width=450, height=50, pady=3)
#    top_frame.grid(row=0)
#    center = ttk.Frame(root, bg='gray2', width=250, height=40, padx=3, pady=3)
 #   center.grid(row=1, sticky="nsew")

    mc = mclb.Multicolumn_Listbox(root, ["Cozmo Command", "Property", "Value"], stripped_rows=("#D4E6F1", "#A9CCE3"), command=on_select) #, cell_anchor="center")
    mc.interior.pack( side = "left" )

#Initialize table
    mc.clear()
    for i in range(len(cozmoCommands)):
        mc.insert_row([" ", " ", " "])
    mc.column[0] = cozmoCommands

    root.mainloop()

    '''    
        mainframe = ttk.Frame(root, padding=(5, 5, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
    
    
    
    
        lbox = Listbox(mainframe, height=5)
    
    
    
        lbox.grid(column=0, row=1, rowspan=8, sticky=(N, S, E, W))
        for i in range(len(cozmoConSum)):
            lbox.insert(END, cozmoConSum[i])
            if i % 2 == 0:
                lbox.itemconfigure(i, background='#f0f0ff')
    
        ttk.Button(mainframe, text="Cozmo Talks").grid(column=3, row=1, sticky=W)
        ttk.Button(mainframe, text="Cozmo Moves").grid(column=3, row=2, sticky=W)
        ttk.Button(mainframe, text="Cozmo Counts").grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text="Cozmo Square Dancing").grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text="Quit", command=exit).grid(column=4, row=6, sticky=W)
    
        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    
    #    root.bind('<Return>', calculate)
        root.mainloop()
        
   


    mc.insert_row([1, 2, 3])
    show_info("mc.insert_row([1,2,3])")

    mc.row.insert([4, 5, 7])
    show_info("mc.row.insert([4,5,7])")

    mc.update_row(0, [7, 8, 9])
    show_info("mc.update_row(0, [4,5,6])")

    mc.update([[1, 2, 3], [4, 5, 6]])
    show_info("mc.update([[1,2,3], [4,5,6]])")

    mc.select_row(0)
    show_info("mc.select_row(0)")

    print("mc.selected_rows")
    print(mc.selected_rows)
    print("\n")

    print("mc.table_data")
    print(mc.table_data)
    print("\n")

    print("mc.row[0]")
    print(mc.row[0])
    print("\n")

    print("mc.row_data(0)")
    print(mc.row_data(0))
    print("\n")

    print("mc.column[1]")
    print(mc.column[1])
    print("\n")

    print("mc[0,1]")
    print(mc[0, 1])
    print("\n")

    mc.column[1] = ["item1", "item2"]

    mc.update_column(0, cozmoCommands )
    show_info("mc.update_column(2, [8,9])")

    mc.clear()
    show_info("mc.clear()")

    mc.table_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
    show_info("mc.table_data = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]")

    mc.delete_row(1)
    show_info("mc.delete_row(1)")

    row = mc.row[0].update([2, 4, 5])
    show_info("mc.row[0].update([2,4,5])")
 '''



    '''
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
                cozmo.run_program(cozmo_talk)
            elif option == 2:
                cozmo.run_program(cozmo_left_turn)
            elif option == 3:
                cozmo.run_program(cozmo_count)
            elif option == 4:
                cozmo.run_program(cozmo_drive_square)
    '''



if __name__ == "__main__":
    main()