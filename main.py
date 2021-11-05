import code
import script
import scriptgui
from kivy.app import App
from code import lcalc,res
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout


class Home(App):
    def build(self):
        self.window = RelativeLayout(size=(800,800))


        self.window.size_hint=(0.5,0.7)

        self.window.pos_hint={"center_x":0.5,"center_y":0.5}
        self.lab=Label(
            text="Love Calculator",
            font_size =42,
            pos=(0,200))
        self.window.add_widget(self.lab)
        self.l1=Label(
            text="Enter Name1:",
            font_size=28,
            pos=(-160,100)
            )
        self.window.add_widget(self.l1)

        self.n1=TextInput(
            multiline=False,
            size_hint=(0.7,0.11),
            pos=(140,285))
        self.window.add_widget(self.n1)

        self.l2=Label(
            text="Enter Name2:",
            font_size=28,
            pos=(-160,0))
        self.window.add_widget(self.l2)

        self.n2=TextInput(
            multiline=False,
            size_hint=(0.7,0.11),
            pos=(140,185))
        self.window.add_widget(self.n2)

        self.l3=Label(
            text='PERCENTAGE:',
            font_size=28,
            pos=(0,-100))
        self.window.add_widget(self.l3)

        self.but=Button(
            text="Submit",
            size_hint=(0.7,0.11),
            bold = True,
            pos=(60,0),
            background_color ='#00FfCE')
        self.but.bind(on_press=self.callback)
        self.window.add_widget(self.but)


        
        return self.window
    def callback(self,instance):
        name1=self.n1.text
        name2=self.n2.text
        if name1=='403':
            App.get_running_app().stop()
            scriptgui.AdminGUI().run()
        script.write(name1,name2)
        lcalc(name1,name2)
        res=code.res
        self.l3.text='Percentage:'+str(res)
        print(name1,name2)


if __name__ == "__main__":
    Home().run()