#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 18:09:59 2022

@author: henrymouawad
"""
# simple calculator using tkinter package


# import packages
import tkinter as tk
from operator import add, truediv, mul, sub, __pow__
import math

# create root
root = tk.Tk()
root.title("Simple Calculator")
root.configure(background='blue')

# square root function with 2 inputs in order to keep the functionality of the
# button_equal function consistent across operation types
def sqrt(a, b):
    return math.sqrt(a)


# create entry box
e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=0)

# operations dict will hold string versions of the calculator functions available
# we use a dict to store the value and map it to a corresponding function
# that will be applied to our inputted values in order to avoid conditionals
operations_dict = {"+": add, "-": sub, "*": mul, "/": truediv, "**": __pow__,
                   "√": sqrt}



def button_click(val):
    ''' Function: button_click
        Parameters: val (string)
        Returns: string, representing number input
    '''
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(val))

def button_clear():
    ''' Function: button_clear
        Parameters: 
        Returns: cleared entry box
    '''
    e.delete(0, tk.END)
    

def button_op(operation):
    ''' Function: button_op
        Parameters: operation (string)
        Returns: stores the current input into global variable and clears input
                 box for next input to be entered
    '''
    first_number = e.get()
    global f_num
    global op
    
    op = operations_dict[operation]
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_equal():
    ''' Function: button_equal
        Parameters: 
        Returns: the answer of 2 inputs and a given operation
    '''
    second_number = e.get()
    e.delete(0, tk.END)
    if second_number == "":
        second_number = 0
    
    e.insert(0, op(f_num, float(second_number)))
    

# Define Buttons on Calculator
pad_length = 20

# number buttons
button_1        = tk.Button(root, text="1", padx=pad_length, pady=pad_length, command=lambda: button_click("1"))
button_2        = tk.Button(root, text="2", padx=pad_length, pady=pad_length, command=lambda: button_click("2"))
button_3        = tk.Button(root, text="3", padx=pad_length, pady=pad_length, command=lambda: button_click("3"))
button_4        = tk.Button(root, text="4", padx=pad_length, pady=pad_length, command=lambda: button_click("4"))
button_5        = tk.Button(root, text="5", padx=pad_length, pady=pad_length, command=lambda: button_click("5"))
button_6        = tk.Button(root, text="6", padx=pad_length, pady=pad_length, command=lambda: button_click("6"))
button_7        = tk.Button(root, text="7", padx=pad_length, pady=pad_length, command=lambda: button_click("7"))
button_8        = tk.Button(root, text="8", padx=pad_length, pady=pad_length, command=lambda: button_click("8"))
button_9        = tk.Button(root, text="9", padx=pad_length, pady=pad_length, command=lambda: button_click("9"))
button_0        = tk.Button(root, text="0", padx=pad_length, pady=pad_length, command=lambda: button_click("0"))

# functional buttons
button_decimal  = tk.Button(root, text=".", padx=pad_length, pady=pad_length, command=lambda: button_click("."))
button_equal    = tk.Button(root, text="=", padx=pad_length * 2, pady=pad_length, command = button_equal)
button_clear    = tk.Button(root, text="Clear", padx=pad_length * 2, pady=pad_length, command = button_clear)

# operation buttons
button_subtract = tk.Button(root, text="-", padx=pad_length, pady=pad_length, command= lambda: button_op("-"))
button_multiply = tk.Button(root, text="*", padx=pad_length, pady=pad_length, command= lambda: button_op("*")) 
button_divide   = tk.Button(root, text="/", padx=pad_length, pady=pad_length, command= lambda: button_op("/"))
button_add      = tk.Button(root, text="+", padx=pad_length, pady=pad_length, command= lambda: button_op("+"))
button_sqrt     = tk.Button(root, text="√", padx=pad_length, pady=pad_length, command= lambda: button_op("√"))
button_exp      = tk.Button(root, text="**", padx=pad_length, pady=pad_length, command= lambda: button_op("**"))




# Put the buttons on the screen
# use sticky='nsew' to stick them all together for better visual

# bottom row
button_1.grid(row=3, column=0, sticky='nsew')
button_2.grid(row=3, column=1, sticky='nsew')
button_3.grid(row=3, column=2, sticky='nsew')

# middle row
button_4.grid(row=2, column=0, sticky='nsew')
button_5.grid(row=2, column=1, sticky='nsew')
button_6.grid(row=2, column=2, sticky='nsew')

# top row 
button_7.grid(row=1, column=0, sticky='nsew')
button_8.grid(row=1, column=1, sticky='nsew')
button_9.grid(row=1, column=2, sticky='nsew')

button_0.grid(row=4, column=0, sticky='nsew')

# operations
button_add.grid(row=2, column=3, sticky='nsew')
button_subtract.grid(row=5, column=3, sticky='nsew')
button_multiply.grid(row=3, column=3, sticky='nsew')
button_divide.grid(row=4, column=3, sticky='nsew')
button_sqrt.grid(row=4, column=1, sticky='nsew')
button_exp.grid(row=4, column=2, sticky='nsew')

# functional
button_equal.grid(row=5, column=1, columnspan=2, sticky='nsew')
button_decimal.grid(row=5, column=0, sticky='nsew')
button_clear.grid(row=1, column=3, sticky='nsew')

# run program using .mainloop()
root.mainloop()