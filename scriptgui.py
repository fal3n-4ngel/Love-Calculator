#scriptgui
import os
import time
import script
from script import*
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import  Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout

#color Codes 
# light red = #dc143c
# red = #c61236
# dark= #b01030 , #9a0e2a
# darker = #6e0a1e, #580818, #420612, #2c040c, #160206
data=''
class AdminGUI(App):
    def build(self):
        self.window1 = RelativeLayout(size=(800,800))
        self.window1.size_hint=(0.5,0.7)
        self.window1.pos_hint={"center_x":0.5,"center_y":0.5}
        self.lab=Label(
            text="Love Calculator ADMIN",
            font_size =42,
            color='#b01030',
            pos=(0,200))
        self.window1.add_widget(self.lab)
        self.l1=Label(
            text="Enter CODE:",
            font_size=28,
            pos=(-160,60)
            )
        self.window1.add_widget(self.l1)

        self.n1=TextInput(
            multiline=False,
            size_hint=(0.7,0.11),
            pos=(140,245))
        self.window1.add_widget(self.n1)

        self.l2=Label(
            text="Result",
            font_size=28,
            pos=(0,-50))
        self.window1.add_widget(self.l2)

    
        self.but=Button(
            text="Submit",
            size_hint=(0.7,0.11),
            bold = True,
            pos=(60,50),
            background_color ='#9a0e2a')
        self.but.bind(on_press=self.callback)
        self.window1.add_widget(self.but)
        
        return self.window1


    def callback(self,instance):
        global data
        code=self.n1.text.lower()
        if code == '403':
            script.cod404()
            self.l2.text="Wiped...."
        elif code=='exit' or code =='quit':
            exit()
        elif code=='open':
            self.l2.text="Opened."
            cmd='notepad.exe data.txt'
            os.system(cmd)
            self.l2.text="Opening.."
        else:
            self.l2.text="Invalid Cmd"

