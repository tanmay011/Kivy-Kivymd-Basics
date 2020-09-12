# Adding images in bg

from kivy.app import App
from kivy.uix.image import Image,AsyncImage

class TestApp(App):
    def build(self):
        # img = Image(source='delta.png')
        img = AsyncImage(source='https://image.shutterstock.com/image-photo/mountains-during-sunset-beautiful-natural-260nw-407021107.jpg')
        return img

        
TestApp().run()