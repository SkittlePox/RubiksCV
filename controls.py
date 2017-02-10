#!/usr/bin/env python
from Tkinter import *
import tkMessageBox
import numpy as np

# Tkinter Color Change
red_floor = [156, 220, 65]
red_ceil = [180, 250, 110]
green_floor = [32, 16, 69]
green_ceil = [104, 83, 255]
orange_floor = [7, 173, 109]
orange_ceil = [17, 255, 255]

color_floors = [red_floor, green_floor, orange_floor]
color_ceils = [red_ceil, green_ceil, orange_ceil]

active_color = 2

root = Tk()

hue = Label(root, text="Hue:")
hue.grid(row=0, column=0)
saturation = Label(root, text="Saturation:")
saturation.grid(row=0, column=2)
value = Label(root, text="Value:")
value.grid(row=0, column=4)
color_label = Label(root, text="Color:")
color_label.grid(row=2, column=0)
blur_label = Label(root, text="Blur:")
blur_label.grid(row=2, column=1)
erode_label = Label(root, text="Erode:")
erode_label.grid(row=2, column=2)
poly_label = Label(root, text="Poly Appx:")
poly_label.grid(row=2, column=3)
area_label = Label(root, text="Area Thresh:")
area_label.grid(row=2, column=4)

hue_scale_floor = Scale(root, from_=0, to=180, orient=VERTICAL, length=300)
hue_scale_floor.grid(row=1, column=0)
hue_scale_ceil = Scale(root, from_=0, to=180, orient=VERTICAL, length=300)
hue_scale_ceil.grid(row=1, column=1)
saturation_scale_floor = Scale(root, from_=0, to=255, orient=VERTICAL, length=300)
saturation_scale_floor.grid(row=1, column=2)
saturation_scale_ceil = Scale(root, from_=0, to=255, orient=VERTICAL, length=300)
saturation_scale_ceil.grid(row=1, column=3)
value_scale_floor = Scale(root, from_=0, to=255, orient=VERTICAL, length=300)
value_scale_floor.grid(row=1, column=4)
value_scale_ceil = Scale(root, from_=0, to=255, orient=VERTICAL, length=300)
value_scale_ceil.grid(row=1, column=5)
color_scale = Scale(root, from_=0, to=len(color_floors)-1, orient=HORIZONTAL, length=100)
color_scale.grid(row=3, column=0)
blur_scale = Scale(root, from_=2, to=30, orient=HORIZONTAL, length=100, resolution=2)
blur_scale.grid(row=3, column=1)
erode_scale = Scale(root, from_=2, to=30, orient=HORIZONTAL, length=100, resolution=2)
erode_scale.grid(row=3, column=2)
poly_scale = Scale(root, from_=4, to=12, orient=HORIZONTAL, length=100, resolution=1)
poly_scale.grid(row=3, column=3)
area_scale = Scale(root, from_=1, to=30, orient=HORIZONTAL, length=100, resolution=1)
area_scale.grid(row=3, column=4)

def init():
    hue_scale_floor.set(color_floors[active_color][0])
    hue_scale_ceil.set(color_ceils[active_color][0])
    saturation_scale_floor.set(color_floors[active_color][1])
    saturation_scale_ceil.set(color_ceils[active_color][1])
    value_scale_floor.set(color_floors[active_color][2])
    value_scale_ceil.set(color_ceils[active_color][2])
    color_scale.set(active_color)
    blur_scale.set(2)
    erode_scale.set(4)
    poly_scale.set(7)
    area_scale.set(2)

def main():
    root.update_idletasks()
    root.update()
    global active_color
    if(active_color != color_scale.get()):
        active_color = color_scale.get()
        init()
    return color_scale.get, np.array([hue_scale_floor.get(), saturation_scale_floor.get(), value_scale_floor.get()]), np.array([hue_scale_ceil.get(), saturation_scale_ceil.get(), value_scale_ceil.get()]), blur_scale.get()+1, erode_scale.get()+1, poly_scale.get()*0.01, area_scale.get()*100
