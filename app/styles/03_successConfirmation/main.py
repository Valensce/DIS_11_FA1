import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
#set up the mygrid before the myapp
#make sure all the objects are created before the app is, which runs them
#keyword arguments is kwargs

class MyGrid(GridLayout):
    take = ObjectProperty(None)
    dine = ObjectProperty(None)
    orders = ObjectProperty(None)

    def pressed(this):
        taketext = this.take.text
        dinetext = this.dine.text
        orderstext = this.orders.text

        print(taketext)
        print(dinetext)
        print(orderstext)
        
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    MyApp().run() 