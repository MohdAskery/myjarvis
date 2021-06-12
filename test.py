# importing the module
import screen_brightness_control as sbc

# get current brightnessvalue
print(sbc.get_brightness())

#set brightness to 50%
sbc.set_brightness(90)

print(sbc.get_brightness())
