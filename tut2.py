# button tutorials
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='This is Button',size_hint=(0.2,0.2),color=(1,0,0,1),font_size='20sp',pos_hint={'center_x':0.5, 'y':0.5},on_press=self.printpress, on_release=self.printrelease)

    def printpress(self,obj):
        print("Button is pressed")

    def printrelease(self,obj):
        print("Button is released")


TestApp().run()