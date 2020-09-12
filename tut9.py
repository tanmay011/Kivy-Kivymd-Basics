  
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton,MDRectangleFlatButton,MDIconButton
from kivymd.uix.screen import Screen


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn1 = MDFlatButton(text='Hello World', pos_hint={'x': 0, 'y': 0})
        btn = MDFloatingActionButton(icon="android",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                     )
        btn2 = MDIconButton(icon='language-python',pos_hint={'x': 0.5, 'y': 0.5})
        screen.add_widget(btn1)
        screen.add_widget(btn)
        screen.add_widget(btn2)
        return screen


DemoApp().run()