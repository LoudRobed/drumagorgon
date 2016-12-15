import kivy
import cython

import kivy

kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label

__appName__ = 'Drumagorgon'


class MyApp(App):
    def build(self):
        return Label(text='Welcome to {}'.format(__appName__))


if __name__ == '__main__':
    MyApp().run()
