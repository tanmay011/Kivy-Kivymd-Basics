# Taking Input Text

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class TestApp(App):
    def build(self):
        layout = GridLayout(cols=2,row_force_default=True,row_default_height=40, spacing=10,padding=20)
        self.weignt = TextInput(text='Enter weight Here')
        self.height = TextInput(text='Enter height Here')
        submit = Button(text='submit', on_press=self.submit)
        layout.add_widget(self.weignt)
        layout.add_widget(self.height)
        layout.add_widget(submit)
        return layout

    def submit(self,obj):
        print("weight: "+ self.weignt.text)
        print("height: "+ self.height.text)



TestApp().run()
