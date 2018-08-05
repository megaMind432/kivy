from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class SimpleLabel(App):
    def build(self):
        return Button(text="This is a Button")


if __name__ == '__main__':
    SimpleLabel().run()
