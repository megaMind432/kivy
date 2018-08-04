from kivy.app import App

# importing Button object
from kivy.uix.button import Button

class SimpleButton(App):
    def build(self):
        return Button(text = "This is Button! Press the Mouse")


if __name__ == "__main__":
    SimpleButton().run()
