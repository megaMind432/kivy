from kivy.app import App
from kivy.uix.label import Label


class SimpleLabel(App):
    def build(self):
        return Label(text='This is a Label')


if __name__ == '__main__':
    SimpleLabel().run()
