from kivy.app import App
from kivy.uix.label import Label

class Hello(App):
    def build(self):
        return Label(text="hello")

Hello().run()
