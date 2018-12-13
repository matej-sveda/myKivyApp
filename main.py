import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

class myKivyApp(App):

    def build(self):
        return MainWidget()

if __name__ == "__main__":
    myKivyApp().run()
