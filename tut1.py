# Label tutorials
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

class TestApp(App):
    def build(self):
        return Label(text='Hello World', font_size='40sp',bold=True,italic=True,color=(1,0,0,1))

TestApp().run()