#!/usr/bin/kivy
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os.path import dirname, join, isfile, exists

class FooScreen(Screen):
    # 'content' refers to the id of the BoxLayout in FooScreen in foo.kv
    def add_widget(self, *args):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args)
        return super(FooScreen, self).add_widget(*args)

class FooApp(App):
    def build(self):
        self.title = 'Foo'

        # Setting up screens for screen manager
        self.screens = {}
        self.available_screens = ([
            'MainMenu', 'Magic'])  # Backup
        self.screen_names = self.available_screens
        curdir = dirname(__file__)
        self.available_screens = [join(curdir,
            '{}.kv'.format(fn)) for fn in self.available_screens]
        self.go_screen(0)

    # Go to other screen
    def go_screen(self, idx):
        print("Change MainScreen to: {}".format(idx))
        self.index = idx
        # Go to not main menu
        if idx == 0:
            self.root.ids.sm.switch_to(self.load_screen(idx), direction='right')
        # Go to main menu
        else:
            # Only load learnkanji.py when the screen is called
            #if idx == 1:
            #    import data.screens.learnkanji
            self.root.ids.sm.switch_to(self.load_screen(idx), direction='left')

    def load_screen(self, index):
        if index in self.screens:
            return self.screens[index]
        screen = Builder.load_file(self.available_screens[index].lower())
        self.screens[index] = screen
        return screen


if __name__ == '__main__':
    FooApp().run()
