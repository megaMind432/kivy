# kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


# Class for the visible screen with Grid of 2 cols
class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        # Widget for the username part
        self.add_widget(Label(text='Username: '))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # Widget for the password part
        self.add_widget(Label(text='Password: '))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        # Widget for the two way auth
        self.add_widget(Label(text='Two way Auth '))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)


# main class for creating the window
class SimpleKivy(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    SimpleKivy().run()
