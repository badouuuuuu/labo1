#! /usr/bin/python3

import sys


from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (1024, 768)
Window.minimum_width, Window.minimum_height = Window.size

runTouchApp(Builder.load_string("""

BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        size_hint: 1, .1
        padding: 20
        spacing: 20
        canvas.before:
            Color:
                rgba: (0,0,0.53,0.2)
            Rectangle:
                size: self.size
                pos: self.pos

        Button:
            text: "Add User"
        Button:
            text: "Modify User"
        Button:
            text: "Add Menu"
        Button:
            text: "Modify Menu"

    BoxLayout:
        size_hint: 1, 1
        padding: 40
        spacing: 40

        canvas.before:
            Color:
                rgba: (0,0,0.53,0.2)
            Rectangle:
                size: self.size
                pos: self.pos
        Label:
            text: "INFO DATABASE ICI"

    
        GridLayout:
            padding: 2
            spacing:4
            canvas.before:
                Color:
                    rgba: (0,0,0.53,0.2)
                    
            cols: 3

            Button:
                text: "7"
            Button:
                text: "8"
            Button:
                text: "9"
            Button:
                text: "4"
            Button:
                text: "5"
            Button:
                text: "6"      
            
            Button:
                text: "1"
            Button:
                text: "2"
            Button:
                text: "3"      

            Button:
                text: "0"
            Button:
                text: "."
 
            Button:
                text: "Cancel"
                background_color: (1.0, 0.0, 0.0, 1.0)
                
            Button:
                text: "Enter"
                background_color: (0, 200, 0, .5)
   


"""))
