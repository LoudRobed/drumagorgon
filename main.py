import kivy
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.bubble import Button
from engine import recorder

kivy.require('1.0.6')


__appName__ = 'Drumagorgon'


def callback(instance):
    Logger.info("Dette skjedde")
    recorder.record()


class RootScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(RootScreen, self).__init__(**kwargs)
        btn1 = Button(text='Play')
        btn1.bind(on_press=callback)
        self.add_widget(btn1)


class MyApp(App):
    def build(self):
        return RootScreen()


if __name__ == '__main__':
    MyApp().run()
